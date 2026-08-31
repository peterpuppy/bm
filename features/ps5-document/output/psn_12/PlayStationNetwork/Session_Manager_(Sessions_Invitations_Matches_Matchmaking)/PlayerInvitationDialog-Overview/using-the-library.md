# PlayerInvitationDialog Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayerInvitationDialog-Overview/using-the-library.html

# Using the Library

This topic describes the preparations required to use the PlayerInvitationDialog library and the basic procedure for sending invitations using the PlayerInvitationDialog library.

# Preparation

To use the PlayerInvitationDialog library, the `sceCommonDialogInitialize()` function for initializing the CommonDialog library must be called once upon program startup to start a common dialog process.

Note that this step is not necessary if it is already running; `SCE_COMMON_DIALOG_ERROR_ALREADY_SYSTEM_INITIALIZED` will return if `sceCommonDialogInitialize()` is called when a common dialog process is already running.

Note:

Call `sceCommonDialogInitialize()` upon program startup, as it may take some time for a common dialog process to start. Moreover, since file reads will occur when a common dialog process starts, the file load speed of the application process may be affected. Be sure to implement the application so that the waiting time does not seem excessively long for the user.

For details on initializing the CommonDialog library, refer to the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document and [CommonDialog Library Reference](../CommonDialog-Reference/__document_toc.html) document.

# Basic Procedure

The following is a description of the basic procedure for sending invitations using the PlayerInvitationDialog library. The processing flow is summarized as follows:

1. [Initialize the player invitation dialog](basic-procedure.html#player-invitation-dialog-library-overview_1_2__basic_procedure_1): `scePlayerInvitationDialogInitialize()`
2. [Set player invitation dialog parameters](basic-procedure.html#player-invitation-dialog-library-overview_1_2__basic_procedure_2): `scePlayerInvitationDialogParamInitialize()`, `ScePlayerInvitationDialogParam`
3. [Display the player invitation dialog](basic-procedure.html#player-invitation-dialog-library-overview_1_2__basic_procedure_3): `scePlayerInvitationDialogOpen()`
4. [Obtain the player invitation dialog call result](basic-procedure.html#player-invitation-dialog-library-overview_1_2__basic_procedure_4): `scePlayerInvitationDialogGetResult()`, `ScePlayerInvitationDialogResult`
5. [Terminate the player invitation dialog](basic-procedure.html#player-invitation-dialog-library-overview_1_2__basic_procedure_5): `scePlayerInvitationDialogTerminate()`

1. **Initialize the player invitation dialog**

   Initialize the player invitation dialog with `scePlayerInvitationDialogInitialize()`.

   ```
   if ( scePlayerInvitationDialogInitialize() < 0 ) {
       // Error handling
   }
   ```
2. **Set player invitation dialog parameters**

   Prepare the `ScePlayerInvitationDialogParam` structure and initialize it with `scePlayerInvitationDialogParamInitialize()`. After initialization, set the required parameters such as the user IDs of users to send invitations to, the player invitation dialog display mode, etc.

   ```
   ScePlayerInvitationDialogParam param;
   scePlayerInvitationDialogParamInitialize( &param );
   param.userId = user_id;    // Obtain in advance
   param.mode = SCE_PLAYER_INVITATION_DIALOG_MODE_SEND;

   ScePlayerInvitationDialogSendParam sendParam;
   memset(&sendParam, 0, sizeof(sendParam));
   sendParam.sessionId = session_id_from_server;    // Obtain in advance
   param.sendParam = &sendParam;
   ```

   For details on parameters, refer to the [PlayerInvitationDialog Library Reference](../PlayerInvitationDialog-Reference/__document_toc.html) document..
3. **Display the player invitation dialog**

   Call `scePlayerInvitationDialogOpen()` with the parameters set in step [2](basic-procedure.html#player-invitation-dialog-library-overview_1_2__basic_procedure_2) as arguments. This will display the player invitation dialog and enable the receiving of user operations.

   ```
   if ( scePlayerInvitationDialogOpen( &param ) < 0 ) {
       // Error handling
   }
   ```

   After `scePlayerInvitationDialogOpen()` terminates normally, call `scePlayerInvitationDialogUpdateStatus()` at regular intervals (for example, at every rendering frame) to poll the operation status of the dialog.

   ```
   while(1) {
       stat = scePlayerInvitationDialogUpdateStatus();
       if( stat == SCE_COMMON_DIALOG_STATUS_FINISHED ) {
           break;
       } else if( stat == SCE_COMMON_DIALOG_STATUS_RUNNING ) {
           if( need_close ) {
               scePlayerInvitationDialogClose();
               break;
           }
       }
   }
   ```

   `SCE_COMMON_DIALOG_STATUS_RUNNING` returns while the dialog is being displayed. Wait until the dialog is closed and the operation status becomes `SCE_COMMON_DIALOG_STATUS_FINISHED`.
4. **Obtain the player invitation dialog call result**

   When the operation status transitions to `SCE_COMMON_DIALOG_STATUS_FINISHED`, obtain the call result with `scePlayerInvitationDialogGetResult()`.

   ```
   ScePlayerInvitationDialogResult result;
   memset( &result, 0, sizeof(result) );
   if( scePlayerInvitationDialogGetResult( &result ) < 0 ) {
       // Error handling
   }
   ```

   To display the player invitation dialog again after obtaining the call result, return to step [2](basic-procedure.html#player-invitation-dialog-library-overview_1_2__basic_procedure_2) and start again from setting the parameters.
5. **Terminate the player invitation dialog**

   Once you've obtained the call result and no longer require the player invitation dialog, call `scePlayerInvitationDialogTerminate()` to perform termination processing. This will free the resources allocated upon initialization, and the operation status of the dialog will transition to `SCE_COMMON_DIALOG_STATUS_NONE`.

   Note:

   `scePlayerInvitationDialogOpen()` can also be called when the operation status of the dialog is `SCE_COMMON_DIALOG_STATUS_FINISHED`. Thus, it is possible to display the dialog again without having to first execute `scePlayerInvitationDialogTerminate()` and terminate the dialog.

## Closing the Dialog from the Application

Call `scePlayerInvitationDialogClose()` to close the player invitation dialog without waiting for user operation. When the call of this function succeeds and `scePlayerInvitationDialogUpdateStatus()` is periodically called thereafter, the dialog will carry out processing to close the dialog display; the operation status will transition to `SCE_COMMON_DIALOG_STATUS_FINISHED` upon processing completion.

When the dialog is closed with `scePlayerInvitationDialogClose()`, the dialog call result that can be obtained with `scePlayerInvitationDialogGetResult()` will be `SCE_COMMON_DIALOG_RESULT_OK`.

## Abort Processing

To perform an emergency abort of the player invitation dialog processing from the application, call `scePlayerInvitationDialogTerminate()`. The processing will end immediately and the operation status of the dialog will transition to `SCE_COMMON_DIALOG_STATUS_NONE`.

## Handling of Unexpected Fatal Errors

There is a possibility that the following functions will return `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL`. In such cases, call `scePlayerInvitationDialogTerminate()`. It will then become possible to re-execute the processing from step [1](basic-procedure.html#player-invitation-dialog-library-overview_1_2__basic_procedure_1).

* `scePlayerInvitationDialogInitialize()`
* `scePlayerInvitationDialogOpen()`
* `scePlayerInvitationDialogGetResult()`