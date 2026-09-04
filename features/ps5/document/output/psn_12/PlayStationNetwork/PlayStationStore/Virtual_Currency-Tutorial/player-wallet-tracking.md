# Virtual Currency Tutorial – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Virtual_Currency-Tutorial/player-wallet-tracking.html

# Code Walkthrough

This chapter provides a walkthrough of the code used within the tutorial application.

# Initialization of Frameworks

This topic provides details on the application's initialization code.

The snippet below shows the initialization code performed by the application. The main modules initialized early on are the NpAuth, NpCommerce, NpEntitlementAccess, NpCppWebAPI, and CommonDialog.

```
sceSysmoduleLoadModule(SCE_SYSMODULE_NP_AUTH);
sceSysmoduleLoadModule(SCE_SYSMODULE_NP_COMMERCE);
sceSysmoduleLoadModule(SCE_SYSMODULE_NP_ENTITLEMENT_ACCESS);
sceSysmoduleLoadModule(SCE_SYSMODULE_NP_CPP_WEB_API);

sceCommonDialogInitialize();

SceNpEntitlementAccessInitParam initParam;
SceNpEntitlementAccessBootParam bootParam;
memset(&initParam, 0, sizeof(SceNpEntitlementAccessInitParam));
memset(&bootParam, 0, sizeof(SceNpEntitlementAccessBootParam));

sceNpEntitlementAccessInitialize(&initParam, &bootParam);

sce::Np::CppWebApi::Common::LibContext *cppWebApiLibContext = new sce::Np::CppWebApi::Common::LibContext();
sce::Np::CppWebApi::Common::InitParams webApiInitParams;
sce::Np::CppWebApi::Common::initialize(webApiInitParams, *cppWebApiLibContext);
```

You must initialize these modules early in the flow to ensure the modules are fully initialized and available for use when the user triggers the associated flow.

# Creating the In-Game Store

This topic describes the process for creating the in-game store, as well as explanations for the code used.

There are a few steps involved in creating a compliant in-game store experience while doing commerce on the PlayStation™Network platform:

* Display the PlayStation™Store icon.
* Initialize the commerce dialog.
* Get catalog and product information.
* Adhere to pricing display rules.
* Retrieve player wallet information.

## Displaying the PlayStation™Store Icon and Commerce Dialog Initialization

Whenever you display PlayStation™Store products in game you must use the `sceNpCommerceShowPsStoreIcon()` function to display the PlayStation™Store icon. When you have finished displaying products you can dismiss the icon by calling `sceNpCommerceHidePsStoreIcon()`.

Use the `sceNpCommerceDialogInitialze()` method to initialize the NpCommerceDialog. This function must be called before you can invoke the commerce dialog. Before using any other common dialogs you must call `sceNpCommerceDialogTerminate()`.

```
void ScreenStore::enter()
{
    sceNpCommerceShowPsStoreIcon(SCE_NP_COMMERCE_PS_STORE_ICON_RIGHT);
    sceNpCommerceDialogInitialize();

    ...
}

void ScreenStore::exit()
{
    ...

    sceNpCommerceDialogTerminate();
    sceNpCommerceHidePsStoreIcon();
}
```

## Getting Catalog and Product Information

Some classes are used in the application to retrieve and display catalog and product information in the application in a multi-threaded fashion.

The `StoreCatalog` singleton class provides methods to get the catalog and product information. It also allows subscribing classes to get access to this information by registering with it, passing in an object of type `StoreCatalogListener`. The `ScreenStore` class implements the `StoreCatalogListener` interface.

```
class StoreCatalogListener
{
public:
    virtual void OnCatalogPopulated(ProductListPtr products) = 0;
    virtual void OnCatalogError(int error) = 0;
};
```

On entry to ScreenStore it registers itself with the StoreCatalog, checks for cached product data, and if necessary, requests a catalog refresh.

```
void ScreenStore::enter()
{
    sceNpCommerceShowPsStoreIcon(SCE_NP_COMMERCE_PS_STORE_ICON_RIGHT);
    sceNpCommerceDialogInitialize();

    auto catalog = StoreCatalog::getInstance();
    catalog->registerListener(this);

    if (catalog->getProducts())
    {
        OnCatalogPopulated(catalog->getProducts());
    }

    if (!catalog->isUpdating())
    {
        catalog->refreshCatalog();
    }

    ...
}
```

When catalog products are cached they are passed to `OnCatalogPopulated()` so ScreenStore can create new StoreProduct UI elements representing each product.

```
void ScreenStore::OnCatalogPopulated(ProductListPtr products)
{
    clearProducts();

    for (auto it = products->begin(); it != products->end(); ++it)
    {
        auto productData = (*it);
        auto product = new StoreProduct(productData);
        m_products.push_back(product);
        addElement(product);
    }
}
```

The `StoreCatalog` singleton uses a background thread task called `GetContainerJob` to refresh product data. `GetContainerJob` derives from the `JobItem` class provided by the SampleUtil framework and uses the `NpCppWebApi` library to retrieve product data.

```
using namespace sce::Np::CppWebApi;
typedef Common::IntrusivePtr<Common::Vector<ContainerPtr>> ContainerListPtr;

class GetContainerJob : public sce::SampleUtil::Helper::JobItem
{
public:
    GetContainerJob(StoreCatalog *catalog, Common::LibContext* apiLibContext, int32_t userContextId)
        : JobItem("SceNpCommerceSampleJob")
        , m_catalog(catalog)
        , m_webapiUserCtxId(userContextId)
        , m_cppWebApiLibContext(apiLibContext)
    {
    }

protected:
    virtual int run()
    {
        Common::Transaction<ContainerListPtr> transaction;
        int ret = transaction.start(m_cppWebApiLibContext);
        SCE_SAMPLE_UTIL_ASSERT_EQUAL(ret, SCE_OK);
        if (ret != SCE_OK)
        {
            return ret;
        }

        InGameCatalog::V5::ContainerApi::ParameterToGetContainer param;
        ret = param.initialize(m_cppWebApiLibContext);
        SCE_SAMPLE_UTIL_ASSERT_EQUAL(ret, SCE_OK);

        param.setserviceLabel(0);

        ret = InGameCatalog::V5::ContainerApi::getContainer(m_webapiUserCtxId, param, transaction);

        if (ret == SCE_OK)
        {
            ret = transaction.getResponse(m_response);
            SCE_SAMPLE_UTIL_ASSERT_EQUAL(ret, SCE_OK);
        }

        int ret2 = SCE_OK;
        if (param.isInitialized())
        {
            ret2 = param.terminate();
            SCE_SAMPLE_UTIL_ASSERT_EQUAL(ret2, SCE_OK);
        }

        ret2 = transaction.finish();
        SCE_SAMPLE_UTIL_ASSERT_EQUAL(ret2, SCE_OK);

        return ret;
    }

    virtual void finish(int result)
    {
        if (result != SCE_OK)
        {
            m_catalog->handleError(result);
            return;
        }

        if ((*m_response).size() > 0)
        {
            auto root = (*m_response)[0];
            m_catalog->populateProducts(root);
        }
    }

private:
    StoreCatalog *m_catalog;
    int32_t m_webapiUserCtxId;
    Common::LibContext* m_cppWebApiLibContext;
    ContainerListPtr m_response;
};
```

## Product Checkout Using NpCommerceDialog

When the user clicks on any product to purchase, the `NpCommerceDialog` opens in the `SCE_NP_COMMERCE_DIALOG_MODE_CHECKOUT` mode.

```
void ScreenStore::openCheckout(const std::string productId)
{
    SceUserServiceUserId userId;
    sceUserServiceGetInitialUser(&userId);

    SceNpCommerceDialogParam param;
    sceNpCommerceDialogParamInitialize(&param);
    param.mode = SCE_NP_COMMERCE_DIALOG_MODE_CHECKOUT;
    param.userId = userId;
    param.numTargets = 1;

    const char* targets[] = { productId.c_str() };
    param.targets = targets;
    sceNpCommerceDialogOpen(&param);
    m_isCommerceDialogOpen = true;
}
```

When the checkout dialog is opened, the `ScreenStore` will call `updateCommerceDialog()` from its `update()` function to monitor the status of the common dialog.

```
int32_t ScreenStore::updateCommerceDialog()
{
    int ret = SCE_OK;
    ret = sceNpCommerceDialogUpdateStatus();
    if (ret < SCE_OK)
    {
        m_isCommerceDialogOpen = false;
        return ret;
    }
    else if (ret == SCE_COMMON_DIALOG_STATUS_FINISHED)
    {
        m_isCommerceDialogOpen = false;

        SceNpCommerceDialogResult dialogResult;
        memset(&dialogResult, 0, sizeof(SceNpCommerceDialogResult));
        ret = sceNpCommerceDialogGetResult(&dialogResult);

        if (ret < SCE_OK)
        {
            return ret;
        }

        if (dialogResult.result == SCE_NP_COMMERCE_DIALOG_RESULT_PURCHASED)
        {
            PlayerWallet::getInstance()->syncWallet();
        }
    }

    return SCE_OK;
}
```

## Adherence to Pricing Rules

This tutorial demonstrates price rendering. For details on the different kind of pricing rules, refer to the [In-Game Catalog Overview](../../../WebAPI/latest/In_Game_Catalog-Overview/__document_toc.html).

In this tutorial application, display logic of products along with price rendering is handled in the `StoreProduct` class.

If the SKU being bought has a PlayStation®Plus discount, the rendering of the price is done differently. It also shows the overlay of the PlayStation®Plus icon in the price.

# Player Wallet Tracking

This topic provides information on how to implement the player wallet tracking feature.

This tutorial application also shows how the game can keep track of the count of virtual currency purchased from the PlayStation™Network by the user. PlayStation™Network policy dictates that all virtual currency must be consumed by a game server in a single transfer of entitlements rather than directly from the game client itself. The `PlayerWallet` singleton class is used to access and maintain the state of the virtual currency purchased by the user from the PlayStation™Network game server.

Like the `StoreCatalog` class, the `PlayerWallet` class allows subscribers of type `PlayerWalletListener` to get access to this data.

```
class PlayerWalletListener
{
public:
    virtual void OnCurrencyAmountUpdate(int currencyAmount) = 0;
    virtual void OnPlayerWalletSyncError(int error, int statusCode) = 0;
};
```

Since the `ScreenStore` class derives from `PlayerWalletListener` class, it can register itself with the `PlayerWallet` class when accessed.

```
void ScreenStore::enter()
{
    ...

    auto wallet = PlayerWallet::getInstance();
    wallet->registerListener(this);

    setPlayerWallet(wallet->getCurrencyAmount());

    if (!wallet->isSyncing())
    {
        wallet->syncWallet();
    }
}
```

## Starting Game Session

All communication between the `PlayerWallet` singleton and the game server is handled through a background thread jobs derived from `GameServerJob` which uses the `Http2` and `Json2` libraries. For more details regarding `Http2` and `Json2` refer to the [Http2 Library Overview](../Http2-Overview/__document_toc.html) and [Json2 Library Overview](../Json2-Overview/__document_toc.html).

For the `PlayerWallet` to establish a connection with the game server it must first create a session. To start a session the game will acquire an authorization code using the `NpAuth` library and pass it to the game server. The game server will exchange the authorization code for an authorization token from the PlayStation™Network and then store the authorization token using a unique session ID. That session ID along with the player's stored currency count will be returned to the game. The game will use this session ID for all future communication with the game server.

Setup Session Flow

```
class StartSessionJob : public GameServerJob
{
public:
    StartSessionJob(PlayerWallet *wallet, SceUserServiceUserId userId, int libHttp2CtxId)
        : GameServerJob("StartSessionJob", libHttp2CtxId)
        , m_wallet(wallet)
        , m_userId(userId)
    {
        snprintf_s(m_uri, sizeof(m_uri) - 1, SESSION_URI_FORMAT, Config::getInstance()->getServerAddress());
    }

protected:
    virtual int addHeaders(int reqId)
    {
        return sceHttp2AddRequestHeader(reqId, "X-PSN-Auth-Code", m_authCode.code, SCE_HTTP2_HEADER_OVERWRITE);
    }

    virtual int run()
    {
        int ret = SCE_OK;
        int reqId = 0;

        SceNpClientId clientId;
        SceNpAuthGetAuthorizationCodeParameterV3 authParam;
        int issuerId = 0;

        ret = sceNpAuthCreateRequest();
        if (ret < 0) 
        {
            return ret;
        }
        reqId = ret;

        memset(&clientId, 0, sizeof(clientId));
        strncpy(clientId.id, GET_AUTHORIZATION_CODE_SAMPLE_CLIENT_ID, SCE_NP_CLIENT_ID_MAX_LEN);

        memset(&authParam, 0, sizeof(authParam));
        authParam.size = sizeof(authParam);
        authParam.userId = m_userId;
        authParam.clientId = &clientId;
        authParam.scope = GET_AUTHORIZATION_CODE_SAMPLE_SCOPE;

        memset(&m_authCode, 0, sizeof(m_authCode));
        ret = sceNpAuthGetAuthorizationCodeV3(reqId, &authParam, &m_authCode, &issuerId);

        sceNpAuthDeleteRequest(reqId);

        if (ret == SCE_OK)
        {
            ret = GameServerJob::run();
        }

        return ret;
    }

    virtual void finish(int result)
    {
        if (result == SCE_OK && m_statusCode == 200)
        {
            m_wallet->onSessionStarted(m_response["sessionId"].getString().c_str());
            m_wallet->updateCurrency(m_response["remainingUseCount"].getInteger(), 0);
        }
        else
        {
            m_wallet->handleSyncError(result, m_statusCode);
        }
    }

private:
    PlayerWallet *m_wallet;
    SceUserServiceUserId m_userId;
    SceNpAuthorizationCode m_authCode;
};
```

## Checking for Un-transferred Entitlements

Whenever the player has un-transferred virtual currency entitlements the game must contact the game server to transfer those entitlements and update the player's currency count. `PlayerWallet` checks for un-transferred entitlements using the `GetEntitlementInfoJob` which uses the `NpEntitlementAccess` library. In `GetEntitlementInfoJob::run()` a request for entitlement info is created which then waits for that request to finish.

```
virtual int run()
{
    int ret = SCE_OK;
    int64_t requestId = 0;

    ret = sceNpEntitlementAccessRequestUnifiedEntitlementInfo(m_userId, 0, &m_entitlementLabel, &requestId);
    if (ret != SCE_OK)
    {
        return ret;
    }

    int result;
    while (1)
    {
        ret = sceNpEntitlementAccessPollUnifiedEntitlementInfo(requestId, &result, &m_entitlementInfo);

        if (ret == SCE_NP_ENTITLEMENT_ACCESS_POLL_RET_FINISHED)
        {
            ret = result;
            break;
        }
        else if (ret != SCE_NP_ENTITLEMENT_ACCESS_POLL_ASYNC_RET_RUNNING)
        {
            break;
        }
    }

    if (requestId > 0)
    {
        sceNpEntitlementAccessDeleteRequest(requestId);
    }

    return ret;
}
```

When the `GetEntitlementInfo` job finishes, if the entitlement `useLimit` is greater than zero it calls the `PlayerWallet::consumeEntitlement()`.

```
virtual void finish(int result)
{
    if (result == SCE_OK)
    {
        if (m_entitlementInfo.useLimit > 0)
        {
            m_wallet->consumeEntitlement(m_entitlementInfo);
        }
    }
    else if (result != SCE_NP_ENTITLEMENT_ACCESS_SERVER_ERROR_ENTITLEMENT_NOT_FOUND)
    {
        m_wallet->handleSyncError(result, 0);
    }
}
```

## Transferring Entitlements

`PlayerWallet::consumeEntitlement()` will use a `ConsumeEntitlementJob` to trigger the Virtual currency entitlement transfer to the game server. When transferring virtual currency entitlements from the PlayStation™Network, the game server must transfer all the available entitlements. After the transfer, the game server will update the player's currency count and return both the amount transferred and the new total to the game. `ConsumeEntitlementJob::finish()` calls `PlayerWallet::updateVirtualCurrency()`.

Transfer Virtual Currency Entitlement Flow

```
virtual void finish(int result)
{
    if (result == SCE_OK && m_statusCode == 200)
    {
        m_wallet->updateCurrency(m_response["remainingUseCount"].getInteger(), m_response["balanceTransferredFromPSN"].getInteger());
    }
    else
    {
        m_wallet->handleSyncError(result, m_statusCode);
    }
}
```

`PlayerWallet::updateVirtualCurrency()` then broadcasts the update to the registered `PlayerWalletListener`. In this example it is ScreenStore which will update the UI.

```
void ScreenStore::OnCurrencyAmountUpdate(int currencyAmount)
{
    setPlayerWallet(currencyAmount);
}
```

## Handling Entitlement Updates

While responding to a player purchasing virtual currency from the in-game store is simple, it is not the only way a player could purchase virtual currency. If you would like to sell virtual currency products from the PlayStation™Store on console, web, or mobile the game can still respond to these purchases using the `SystemService` library. In `PlayerWallet::update()`, `sceSystemServiceGetStatus()` is called to check if there are any events waiting to be processed. If so, `sceSystemServiceReceiveEvent()` retrieves each event. If that event's `eventType` is `SCE_SYSTEM_SERVICE_EVENT_UNIFIED_ENTITLEMENT_UPDATE`, then `PlayerWallet::syncWallet()` is called to begin the consuming flow described above.

```
void PlayerWallet::update()
{
    m_jobQueue->check();

    SceSystemServiceStatus status;
    sceSystemServiceGetStatus(&status);

    SceSystemServiceEvent e;
    for (int i = 0; i < status.eventNum; ++i)
    {
        sceSystemServiceReceiveEvent(&e);

        if (e.eventType == SCE_SYSTEM_SERVICE_EVENT_UNIFIED_ENTITLEMENT_UPDATE 
            && e.data.unifiedEntitlementUpdate.userId == m_userId
            && !isSyncing())
        {
            syncWallet();
        }
    }
}
```