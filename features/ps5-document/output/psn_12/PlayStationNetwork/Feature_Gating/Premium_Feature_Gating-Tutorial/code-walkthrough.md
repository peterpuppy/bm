# Premium Feature Gating Tutorial – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Premium_Feature_Gating-Tutorial/code-walkthrough.html

# Walkthrough of Processing Flow

This chapter provides a walkthrough of the feature gating implementation process.

# Implementing Feature Gating

This topic provides a walkthrough of how to implement feature gating, as well as explanations of the code used in the tutorial game application.

The steps for providing a premium gating feature are as follows:

1. Initialize the Common Dialog in preparation for any in-game commerce scenarios.
2. Perform a premium check for the user, or multiple users logged into the same device.
3. If the premium check fails, encourage upselling of the subscription service using the NP Commerce Dialog.
4. Notify the system of a premium feature being used at certain intervals.
5. Recheck the subscription and handle the situation if the subscription has lapsed.

The representation of this flow is shown below.

Premium Gating Flowchart

## Initialization of the Common Dialog framework

The code snippet below shows the initialization code for the Common Dialog framework. The `sceCommonDialogInitialize()` method initializes the Common Dialog framework. In the tutorial application provided, this logic is included in the main.cpp file on application initialization.

```
void initializeLibraries()
{
    sceSysmoduleLoadModule(SCE_SYSMODULE_ERROR_DIALOG);
    sceErrorDialogInitialize();

    sceCommonDialogInitialize();
    sceSysmoduleLoadModule(SCE_SYSMODULE_NP_COMMERCE);
}
```

Do this early on if you are using in-game commerce. The Common Dialog framework takes some time to load, and initializing it early on ensures the framework is loaded and available for use.

## Checking for Premium

When the flow for a premium feature is initiated, you must execute a check for feature access for each user that will be using the feature. In the snippet below, the `PremiumChecker` class handles this check.

```
void ScreenCheckFeature::enter()
{
    m_state = kState_Initialized;
    m_commerceDialogChecker = nullptr;

    sceNpCommerceDialogInitialize();

    auto session = GameSession::getInstance();
    session->start();

    for (auto it = session->users.begin(); it != session->users.end(); ++it)
    {
        m_userCheckers.push_back(new PremiumChecker((*it)));
    }

    startCheckFeature();
}

void ScreenCheckFeature::startCheckFeature()
{
    int ret;

    for (auto it = m_userCheckers.begin(); it != m_userCheckers.end(); ++it)
    {
        ret = (*it)->start();
        if (ret < 0) 
        {
            openErrorDialog((*it)->userId, ret);
            return;
        }
    }

    m_state = kState_Checking;
}
```

It is important to create an asynchronous request to ensure the main thread isn't blocked. Generate the request ID using `sceNpCreateAsyncRequest()`. This function accepts a parameter of type `SceNpCreateAsyncRequestParameter`.

Use this request ID to invoke the `sceNpCheckPremium()` method shown below. When the request is complete the result will be stored in the provided `SceNpCheckPlusResult`.

```
int32_t PremiumChecker::start()
{
    SceNpCreateAsyncRequestParameter reqParam;
    memset(&reqParam, 0, sizeof(reqParam));
    reqParam.size = sizeof(reqParam);
    reqParam.cpuAffinityMask = SCE_KERNEL_CPUMASK_USER_ALL;
    reqParam.threadPriority = SCE_KERNEL_PRIO_FIFO_DEFAULT;
    int ret = sceNpCreateAsyncRequest(&reqParam);
    if (ret < 0) 
    {
        return ret;
    }

    m_npRequestId = ret;

    SceNpCheckPremiumParameter checkParam;
    memset(&checkParam, 0, sizeof(checkParam));
    checkParam.size = sizeof(checkParam);
    checkParam.features = SCE_NP_PREMIUM_FEATURE_REALTIME_MULTIPLAY;
    checkParam.userId = userId;
    ret = sceNpCheckPremium(m_npRequestId, &checkParam, &m_checkResult);
    if (ret < 0) 
    {
        return ret;
    }

    status = kStatus_Checking;
    return SCE_OK;
}
```

When the request is no longer needed you must abort and free the request by calling `sceNpAbortRequest()`/`sceNpDeleteRequest()`, passing in the request ID.

```
int32_t PremiumChecker::end()
{
    if (m_npRequestId > -1)
    {
        sceNpAbortRequest(m_npRequestId);
        sceNpDeleteRequest(m_npRequestId);
    }

    return SCE_OK;
}
```

## Update/Poll Progress of Each Premium Checker

The following code snippet shows the handling of the asynchronous request for the Premium check call for each user.

The `PremiumChecker` class tracks its own internal state in the status variable. While the status is `kStatus_Checking` the `sceNpPollAsync()` function is called, passing in the request ID and variable to store the return result. If the return value of the function call is `SCE_NP_POLL_ASYNC_RET_FINISHED` then the status is updated to `kStatus_Done` and authorization state for the user is copied from the `m_checkResult` object.

```
int32_t PremiumChecker::update()
{
    if (status == kStatus_Checking)
    {
        int32_t requestResult;
        int32_t res = sceNpPollAsync(m_npRequestId, (int32_t*)&requestResult);

        if (res < 0)
        {
            return res;
        }
        else if (res == SCE_NP_POLL_ASYNC_RET_FINISHED)
        {
            if (requestResult != SCE_OK)
            {
                return requestResult;
            }

            status = kStatus_Done;
            isAuthorized = m_checkResult.authorized;
        }
    }

    return SCE_OK;
}
```

## Encourage Upsell for User That Fails Premium Check

For any user whose premium feature authorization status returned false, display the dialog for upsell using the `SCE_NP_COMMERCE_DIALOG_MODE_PREMIUM` mode and the `SCE_NP_PREMIUM_FEATURE_REALTIME_MULTIPLAY` feature.

```
int32_t ScreenCheckFeature::updateCheckers(SceUserServiceUserId &errorUser)
{
    auto sm = ScreenManager::getInstance();
    int ret;
    bool allAuthorized = true;

    for (auto it = m_userCheckers.begin(); it != m_userCheckers.end(); ++it)
    {
        auto checker = (*it);
        ret = checker->update();
        if (ret < 0) 
        {
            errorUser = checker->userId;
            return ret;
        }

        if (checker->status == PremiumChecker::kStatus_Done && !checker->isAuthorized)
        {
            m_commerceDialogChecker = checker;
            openCommerceDialogPremiumMode(checker->userId);
            return SCE_OK;
        }

        allAuthorized = allAuthorized && (checker->status == PremiumChecker::kStatus_Done && checker->isAuthorized);
    }

    if (allAuthorized)
    {
        sm->changeScreen(kScreenId_Multiplayer);
    }

    return SCE_OK;
}

void ScreenCheckFeature::openCommerceDialogPremiumMode(SceUserServiceUserId user)
{
    int ret = SCE_OK;

    SceNpCommerceDialogParam param;
    sceNpCommerceDialogParamInitialize(&param);
    param.mode = SCE_NP_COMMERCE_DIALOG_MODE_PREMIUM;
    param.userId = user;
    param.features = SCE_NP_PREMIUM_FEATURE_REALTIME_MULTIPLAY;
    ret = sceNpCommerceDialogOpen(&param);

    if (ret < SCE_OK)
    {
        openErrorDialog(user, ret);
    }
    else
    {
        m_state = kState_Upsell;
    }
}
```

## Polling of Commerce Dialog and Result Handling

Once the Common Dialog has been launched, poll for its status. The `ScreenCheckFeature` class tracks its own internal state in the status variable. While the status is `kState_Upsell`, call the `updateCommerceDialog()` function.

Use the `sceNpCommerceDialogUpdateStatus()` function to get the status of the Common Dialog. If the return status is an error, then raise an error using `openErrorDialog()` passing in the `userId` and return value as parameters.

If the return value is `SCE_COMMON_DIALOG_STATUS_FINISHED`, then get the results using the `sceNpCommerceDialogGetResult()` function. The results are stored in `SceNpCommerceDialogResult` and the authorization status of the user can be accessed from it. The code snippet that handles this is shown below.

```
int32_t ScreenCheckFeature::updateCommerceDialog(SceUserServiceUserId &errorUser)
{
    auto sm = ScreenManager::getInstance();
    int ret = sceNpCommerceDialogUpdateStatus();
    if (ret < SCE_OK)
    {
        openErrorDialog(m_commerceDialogChecker->userId, ret);
    }
    else if (ret == SCE_COMMON_DIALOG_STATUS_FINISHED)
    {
        SceNpCommerceDialogResult dialogResult;
        memset(&dialogResult, 0, sizeof(SceNpCommerceDialogResult));
        ret = sceNpCommerceDialogGetResult(&dialogResult);

        if (ret < SCE_OK)
        {
            errorUser = m_commerceDialogChecker->userId;
            return ret;
        }
        
        if (dialogResult.authorized)
        {
            m_commerceDialogChecker->isAuthorized = dialogResult.authorized;
            m_commerceDialogChecker = nullptr;
            m_state = kState_Checking;
        }
        else
        {
            sm->changeScreen(kScreenId_Message);
        }
    }

    return SCE_OK;
}
```

## Notify the System of Premium Feature Usage

Once a user is using a premium feature the system must be periodically notified of the premium feature usage. This tutorial handles this by calling `ScreenMultiplayer::notifyfeature()`.

Use the `sceNpNotifyPremiumFeature()` function, passing the realtime multiplayer feature flag as a parameter. If the player is using in-engine spectating and/or has cross platform play enabled, that information should be provided in the properties bit field of the `SceNpNotifyPremiumFeatureParameter`.

```
void ScreenMultiplayer::notifyFeature()
{
    auto session = GameSession::getInstance();

    SceNpNotifyPremiumFeatureParameter param;
    memset(&param, 0x0, sizeof(param));

    param.size = sizeof(param);
    param.features = SCE_NP_PREMIUM_FEATURE_REALTIME_MULTIPLAY;

    int ret = SCE_OK;
    for (auto it = m_players.begin(); it != m_players.end(); ++it)
    {
        param.properties = SCE_NP_REALTIME_MULTIPLAY_PROPERTY_NONE;

        if (session->allowCrossPlatform)
        {
            param.properties |= SCE_NP_REALTIME_MULTIPLAY_PROPERTY_CROSS_PLATFORM_PLAY;
        }

        if (!it->second.isPlaying)
        {
            param.properties |= SCE_NP_REALTIME_MULTIPLAY_PROPERTY_IN_ENGINE_SPECTATING;
        }

        param.userId = it->first;
        ret = sceNpNotifyPremiumFeature(&param);
        SCE_SAMPLE_UTIL_ASSERT_EQUAL(ret, SCE_OK);
    }

    m_lastNotifyTime = sceKernelGetProcessTime();
}
```

Note:

`sceNpNotifyPremiumFeature()` is a non-blocking call and does not need to be polled.

## Recheck of Subscription

A user's eligibility to use a premium gated feature may change during application execution, based on the state of the account on PlayStation™Network and the status of promotions. Therefore, it is possible for a user who was determined by the premium check to be eligible to use a premium feature to lose this eligibility after proceeding to the feature.

First begin by registering a callback function.

```
void ScreenMultiplayer::enter()
{
    sceNpRegisterPremiumEventCallback(npPremiumEventCallback, (void*)this);

    ...
}
```

The feature check for the user is initiated in the callback function.

```
void npPremiumEventCallback(SceUserServiceUserId userId, SceNpPremiumEventType eventType, void *userData)
{
    if (eventType == SCE_NP_PREMIUM_EVENT_RECHECK_NEEDED)
    {
        ((ScreenMultiplayer*)userData)->startCheck(userId);
    }
}

void ScreenMultiplayer::startCheck(SceUserServiceUserId userId)
{
    auto session = GameSession::getInstance();

    if (session->includesUser(userId))
    {
        auto checker = new PremiumChecker(userId);
        ret = checker->start();
        m_checkers.push_back(checker);
    }
}
```

After initiating the recheck the `PremiumChecker` class is updated as part of the update loop and if the check fails the user is removed from the session. If all players have been removed from a session the game exits the multiplayer mode.

```
void ScreenMultiplayer::update(sce::SampleUtil::Input::PadContext *pad)
{
    auto session = GameSession::getInstance();
    sceNpCheckCallback();
    processUserEvents();

    for (auto it = m_checkers.begin(); it != m_checkers.end();)
    {
        auto checker = (*it);
        ret = checker->update();

        if (checker->status == PremiumChecker::kStatus_Done)
        {
            if (!checker->isAuthorized)
            {
                handleUserLogout(checker->userId);
            }

            checker->end();
            delete checker;
            it = m_checkers.erase(it);
        }
        else
        {
            ++it;
        }
    }

    if (session->users.size() < 1)
    {
        ScreenManager::getInstance()->changeScreen(kScreenId_Message);
        return;
    }

    if (sceKernelGetProcessTime() - m_lastNotifyTime >= NOTIFY_INTERVAL)
    {
        notifyFeature();
    }

    ...
}
```

It is also important to unregister the callback on exit using `sceNpUnregisterPremiumEventCallback()`.

```
void ScreenMultiplayer::exit()
{
    ...
    
    sceNpUnregisterPremiumEventCallback();
}
```

## Handling User Logoffs

While in a mixed local/multiplayer session you might need to handle a local user logging out mid game. If this happens, remove them from the list of players so as to not trigger a `sceNpNotifyPremiumFeature()` call for them after they leave. In `ScreenMultiplayer::update()`, use the `sceUserServiceGetEvent()` function to process any user service events. User service events remain queued until they have been processed by a call to `sceUserServiceGetEvent()`. In this example, only events of type `SCE_USER_SERVICE_EVENT_TYPE_LOGOUT` are considered. When processing events you generally want to continue to handle all events until `sceUserServiceGetEvent()` returns `SCE_USER_SERVICE_ERROR_NO_EVENT`.

```
int ScreenMultiplayer::processUserEvents()
{
    int ret = SCE_OK;
    SceUserServiceEvent event;
    while (1) 
    {
        ret = sceUserServiceGetEvent(&event);
        if (ret == SCE_OK) {
            if (event.eventType == SCE_USER_SERVICE_EVENT_TYPE_LOGOUT) 
            {
                handleUserLogout(event.userId);
            }
        }
        else if (ret == SCE_USER_SERVICE_ERROR_NO_EVENT) 
        {
            break;
        }
        else 
        {
            return ret;
        }
    }

    return SCE_OK;
}
```