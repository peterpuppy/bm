# NpAuthAuthorizedAppDialog Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/NpAuthAuthorizedAppDialog-Overview/preparation.html

# Using the Library

# Preparation

As a prerequisite for using the NpAuthAuthorizedAppDialog library, it is necessary that the user be signed in (able to sign in to the PlayStation™ Network when network conditions are met) and that there be an environment that can connect to the network.

It is also necessary to call the `sceCommonDialogInitialize()` CommonDialog library initialization function one time only when starting the program to first launch the common dialog process. However, if that process has already been started, this step is not required. With the common dialog process started, calling the `sceCommonDialogInitialize()` returns `SCE_COMMON_DIALOG_ERROR_ALREADY_SYSTEM_INITIALIZED`.

Note:

Starting the common dialog process may take some time, so ensure that `sceCommonDialogInitialize()` is called when starting the program. Additionally, file reads and other processes occur when starting the common dialog process, and these may impact the file loading speeds for the current process. Pay attention so that users feel as little delay as possible when loading.

For details about initializing the CommonDialog library, refer to the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) and the [CommonDialog Library Reference](../CommonDialog-Reference/__document_toc.html) documents.

# Basic Procedure

This explains the basic procedure for displaying the NpAuth Authorized App dialog. An overview of the process flow is as follows.

1. [Initializing the NpAuth Authorized App Dialog](basic-procedure.html#np-auth-authorized-app-dialog-library-overview_1_2__li_izp_gnw_ycc): `sceNpAuthAuthorizedAppDialogInitialize()`
2. [Setting NpAuth Authorized App Dialog Parameters](basic-procedure.html#np-auth-authorized-app-dialog-library-overview_1_2__li_dr1_3nw_ycc): `sceNpAuthAuthorizedAppDialogParamInit()`, `SceNpAuthAuthorizedAppDialogParam`
3. [Displaying the NpAuth Authorized App Dialog](basic-procedure.html#np-auth-authorized-app-dialog-library-overview_1_2__li_ybt_wnw_ycc): `sceNpAuthAuthorizedAppDialogOpen()`
4. [Obtaining NpAuth Authorized App Dialog Call Results](basic-procedure.html#np-auth-authorized-app-dialog-library-overview_1_2__li_e2c_4nw_ycc): `sceNpAuthAuthorizedAppDialogGetResult()`, `SceNpAuthAuthorizedAppDialogResult`
5. [Terminating the NpAuth Authorized App Dialog](basic-procedure.html#np-auth-authorized-app-dialog-library-overview_1_2__li_lfs_nnw_ycc): `sceNpAuthAuthorizedAppDialogTerminate()`

Basic Procedure

1. **Initializing the NpAuth Authorized App Dialog**

   Use `sceNpAuthAuthorizedAppDialogInitialize()` to initialize the NpAuth Authorized App dialog.

   ```
   if (sceNpAuthAuthorizedAppDialogInitialize () < 0 ) {
       // Error handling
   }
   ```
2. **Setting NpAuth Authorized App Dialog Parameters**

   Prepare an `SceNpAuthAuthorizedAppDialogParam` structure and initialize it using `sceNpAuthAuthorizedAppDialogParamInit()`. After initialization, set the Authorized App client ID and other required parameters.

   ```
   SceNpAuthAuthorizedAppDialogParam param;
   sceNpAuthAuthorizedAppDialogParamInit ( &param );

   param.userId = user_id; 
   param.authorizedAppClientId = authorized_app_client_id; 
   param.scope = scope;
   param.accessType = SCE_NP_AUTH_ACCESS_TYPE_OFFLINE;
   ```
3. **Displaying the NpAuth Authorized App Dialog**

   Call `sceNpAuthAuthorizedAppDialogOpen()` with the parameters set in [(2)](basic-procedure.html#np-auth-authorized-app-dialog-library-overview_1_2__li_dr1_3nw_ycc) as arguments. This displays the NpAuth Authorized App dialog so that it can accept user operations.

   ```
   if (sceNpAuthAuthorizedAppDialogOpen( &param ) < 0 ) {
       // Error handling
   }
   ```

   After `sceNpAuthAuthorizedAppDialogOpen()` terminates normally, call `sceNpAuthAuthorizedAppDialogUpdateStatus()` at regular intervals (for example, per rendered frame) to poll the operational status of the dialog.

   ```
   while(1) {
       stat = sceNpAuthAuthorizedAppDialogUpdateStatus();
       if( stat == SCE_COMMON_DIALOG_STATUS_FINISHED ) {
           break;
       } else if( stat == SCE_COMMON_DIALOG_STATUS_RUNNING ) {
           if( need_close ) {
               sceNpAuthAuthorizedAppDialogClose();
               break;
           }
       }
       sceKernelUsleep(16666);
   }
   ```

   While the dialog is displayed, `SCE_COMMON_DIALOG_STATUS_RUNNING` is returned as the operational status, so wait until the dialog closes and the status changes to `SCE_COMMON_DIALOG_STATUS_FINISHED`.
4. **Obtaining NpAuth Authorized App Dialog Call Results**

   When the operational status transitions to `SCE_COMMON_DIALOG_STATUS_FINISHED`, results can be obtained with `sceNpAuthAuthorizedAppDialogGetResult()`.

   ```
   SceNpAuthAuthorizedAppDialogResult result;
   memset( &result, 0, sizeof(result) );
   if( sceNpAuthAuthorizedAppDialogGetResult( &result ) < 0 ) {
       // Error handling
   }
   ```

   When the results are `SCE_NP_AUTH_AUTHORIZED_APP_DIALOG_RESULT_CONSENTED`, the Authorization code for the Authorized App for the target user can be obtained using the NpAuth library.

   To display the NpAuth Authorized App dialog after obtaining results, go back to [(2)](basic-procedure.html#np-auth-authorized-app-dialog-library-overview_1_2__li_dr1_3nw_ycc) and repeat from the setting of parameters.
5. **Terminating the NpAuth Authorized App Dialog**

   After obtaining results, call `sceNpAuthAuthorizedAppDialogTerminate`() to perform termination processing. This releases resources allocated during initialization and transitions the operational status to `SCE_COMMON_DIALOG_STATUS_NONE`.

   Note:

   `sceNpAuthAuthorizedAppDialogOpen()` can also be called when the operational status is `SCE_COMMON_DIALOG_STATUS_FINISHED`. Accordingly, the NpAuth Authorized App dialog can be displayed again without executing `sceNpAuthAuthorizedAppDialogTerminate()` to terminate.

## Closing the NpAuth Authorized App Dialog from an Application

To close the NpAuth Authorized App dialog without waiting for a user operation, call `sceNpAuthAuthorizedAppDialogClose()`. By periodically calling `sceNpAuthAuthorizedAppDialogUpdateStatus()` after a successful call, the dialog performs processing to terminate the displaying of itself, and the operational status transitions to `SCE_COMMON_DIALOG_STATUS_FINISHED` when this processing is complete.

If you use `sceNpAuthAuthorizedAppDialogClose()` to close the dialog, the result of the dialog call obtained with `sceNpAuthAuthorizedAppDialogGetResult()` is `SCE_COMMON_DIALOG_RESULT_OK`.

## Aborting Processing

Call `sceNpAuthAuthorizedAppDialogTerminate()` to make the application urgently interrupt the processing of the player selection dialog. This immediately terminates processing, and the operational status immediately transitions to `SCE_COMMON_DIALOG_STATUS_NONE`.

## Dealing with Unexpected Fatal Errors

The following functions may return `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL`. If this occurs, call `sceNpAuthAuthorizedAppDialogTerminate()`. You can then rerun the processing from [(1)](basic-procedure.html#np-auth-authorized-app-dialog-library-overview_1_2__li_izp_gnw_ycc).

* `sceNpAuthAuthorizedAppDialogInitialize()`
* `sceNpAuthAuthorizedAppDialogOpen()`
* `sceNpAuthAuthorizedAppDialogGetResult()`