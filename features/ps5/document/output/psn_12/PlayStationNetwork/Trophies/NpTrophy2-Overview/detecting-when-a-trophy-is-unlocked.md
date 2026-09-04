# NpTrophy2 Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpTrophy2-Overview/detecting-when-a-trophy-is-unlocked.html

# Using the Library

This topic explains how to obtain trophy data and detect when trophies are unlocked using the NpTrophy2 library.

# Preparations for Using the NpTrophy2 Library

To use trophies, a trophy configuration file must be created in advance and placed in the specified location. Refer to [Trophy System Overview - Overview of Application Development - Placement of the Trophy Configuration and UDS Configuration Files](../Trophy_System-Overview/placement-of-the-trophy-configuration-and-uds-configuration.html) for details.

# Initialization of the NpTrophy2 Library

1. **Initialize the UserService Library**

   Initialize the UserService library. Refer to [UserService Library Overview - Using the Library - Basic Procedure](../UserService-Overview/basic-procedure.html) for details.
2. **Set the NP Title ID/NP Title Secret**

   To use the NpTrophy2 library, you must set the NP Title ID and NP Title Secret. Refer to [Np Library Overview - Using the Library - Basic Procedure](../Np-Overview/basic-procedure.html) for details.
3. **Load the NpTrophy2 Module**

   Load the PRX module by calling `sceSysmoduleLoadModule()` with `SCE_SYSMODULE_NP_TROPHY2` specified as the module ID.
4. **Create a Context**

   Call `sceNpTrophy2CreateContext()` to create a context for each user. Normally, create a context when a user logs in to the game. Specify the user ID of the target user and the NP service label. Use the NP service label that you specified when you applied for service.

   Note that the trophy configuration file for the specified NP service label must be placed in the correct location, as described in the "[Preparations for Using the NpTrophy2 Library](advance-preparations.html)" section.

   ```
   SceUserServiceUserId userId;    // Store the appropriate user ID
   SceNpServiceLabel serviceLabel = 0;
   SceNpTrophy2Context context = SCE_NP_TROPHY2_INVALID_CONTEXT;
   ret = sceNpTrophy2CreateContext(&context, userId, serviceLabel, 0);
   if (ret < 0) {
       // Error handling
   }
   ```
5. **Create a Handle**

   Prepare a variable of the `SceNpTrophy2Handle` type and call `sceNpTrophy2CreateHandle()` to create a handle.

   ```
   SceNpTrophy2Handle handle = SCE_NP_TROPHY2_INVALID_HANDLE;
   ret = sceNpTrophy2CreateHandle(&handle);
   if (ret < 0) {
       // Error handling
   }
   ```
6. **Register the Context**

   Call `sceNpTrophy2RegisterContext()` to register the context. It is not possible to obtain trophy data with a context that has not been registered.

   ```
   ret = sceNpTrophy2RegisterContext(context, handle, 0);
   if (ret < 0) {
       // Error handling
   }
   ```

   Because this function's processing takes time, call the function from a subthread. Specifically, processing such as the following is performed.

   * New creation of a trophy record file for each user, or opening an existing file
   * Updating an existing trophy record file if a trophy set version has been updated
   * Setting up the Universal Data System
7. **Destroy the Handle**

   Call `sceNpTrophy2DestroyHandle()` to destroy the handle.

   ```
   ret = sceNpTrophy2DestroyHandle(handle);
   if (ret < 0) {
       // Error handling
   }
   ```

## Timings of Context Creation, Registration, and Destruction

Creation and registration of a context must be performed for each user. Normally, a context is created and registered when a logged-in user joins a game, and then the context is destroyed when the user logs out.

The context of a logged-out user will be invalidated by the system software and become unusable. Even if the same user logs in again, the context will not become valid again, and, therefore, the contexts for users must be destroyed when they log out and created and registered again when they rejoin the game.

# Obtaining Trophy Data

1. **Create a Handle**

   Prepare a variable of the `SceNpTrophy2Handle` type and call `sceNpTrophy2CreateHandle()` to create a handle.

   ```
   SceNpTrophy2Handle handle = SCE_NP_TROPHY2_INVALID_HANDLE;
   ret = sceNpTrophy2CreateHandle(&handle);
   if (ret < 0) {
       // Error handling
   }
   ```
2. **Obtain Trophy Data**

   Call `sceNpTrophy2GetTrophyInfo()` to obtain trophy configuration information and trophy records. Since the processing of this function takes some time, call it in a subthread. As arguments, specify the context, handle, the ID of the relevant trophy, and the structure to store the data obtained.

   ```
   SceNpTrophy2Details details;
   SceNpTrophy2Data data;
   int ret;

   memset(&details, 0x00, sizeof(details));
   memset(&data, 0x00, sizeof(data));

   ret = sceNpTrophy2GetTrophyInfo(context, handle, trophyId, &details, &data);
   if ( ret < 0 ) {
       // Error handling
   }
   ```

   Similarly, you can use `sceNpTrophy2GetGameInfo()` to obtain information about a trophy set and `sceNpTrophy2GetGroupInfo()` to obtain information about a group. Additionally, you can obtain information about multiple trophies at once using `sceNpTrophy2GetTrophyInfoArray()` and obtain information about multiple groups at once using `sceNpTrophy2GetGroupInfoArray()`.
3. **Destroy the Handle**

   Call `sceNpTrophy2DestroyHandle()` to destroy the handle.

   ```
   ret = sceNpTrophy2DestroyHandle(handle);
   if (ret < 0) {
       // Error handling
   }
   ```

# Detecting when a Trophy Is Unlocked

1. **Register a Callback Function**

   You can register a callback function that will be called when a trophy is unlocked by calling `sceNpTrophy2RegisterUnlockCallback()`.

   ```
   void
   unlockCallback(SceNpTrophy2Context context, SceNpTrophy2Id trophyId, void *userdata)
   {
       // Application-specific processing
   }
   int ret;
   ret = sceNpTrophy2RegisterUnlockCallback(unlockCallback, NULL);
   if (ret < 0) {
       // Error handling
   }
   ```
2. **Check if Any Trophies Have Been Unlocked**

   Periodically call `sceNpCheckCallback()` to detect any trophy unlocks that have occurred. If a trophy has been unlocked, the callback function registered with `sceNpTrophy2RegisterUnlockCallback()`will be called in the thread that called `sceNpCheckCallback()`.
3. **Unregister the Callback Function**

   When it is no longer necessary to detect unlocked trophies, call `sceNpTrophy2UnregisterUnlockCallback()` to unregister the callback function.

   ```
   ret = sceNpTrophy2UnregisterUnlockCallback()
   if (ret < 0) {
       // Error handling
   }
   ```

# Context Destruction

1. **Destroy Context**

   When a context is no longer necessary, for example, because the user has logged out, call `sceNpTrophy2DestroyContext()` to destroy the context.

   ```
   int ret;
   SceNpTrophy2Context ctxId;

   // Assuming that an appropriate value is stored in ctxId

   ret = sceNpTrophy2DestroyContext(ctxId);
   if (ret < 0) {
       // Error handling
   }
   ```

# Termination of the NpTrophy2 Library

1. **Unload the PRX**

   When the NpTrophy2 library is no longer needed, call `sceSysmoduleUnloadModule()` with `SCE_SYSMODULE_NP_TROPHY2` specified as the module ID to unload the PRX.