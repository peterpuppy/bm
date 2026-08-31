# PlayerSelectionDialog Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/PlayerSelectionDialog-Overview/basic-procedure.html

# Using the Library

# Preparation

Being in the signed-in state (state in which a connection can be made to the PlayStation™Network if network conditions are met) is a precondition to using the PlayerSelectionDialog library. A network-connected environment is also required.

Moreover, the `sceCommonDialogInitialize()` function for initializing the CommonDialog library must be called once upon program startup to start a common dialog process.

Note that this step is not necessary if it is already running. If `sceCommonDialogInitialize()` is called when a common dialog process is already running, `SCE_COMMON_DIALOG_ERROR_ALREADY_SYSTEM_INITIALIZED` will return.

Note:

Call `sceCommonDialogInitialize()` upon program startup, as it may take some time for a common dialog process to start. Moreover, since file reads, etc. will occur when a common dialog process starts, the file load speed of the application process may be affected. Be sure to implement the application so that waiting time does not seem excessively long for the user.

For details on initializing the CommonDialog library, refer to the [CommonDialog Library Overview](../CommonDialog-Overview/__document_toc.html) document and the [CommonDialog Library Reference](../CommonDialog-Reference/__document_toc.html) document.

# Basic Procedure

This section explains the basic procedure to display the player selection dialog. The processing flow is summarized as follows.

1. [Initialize the player selection dialog](basic-procedure.html#player-selection-dialog-library-overview_1_2__li_dq3_mnj_gbc): `scePlayerSelectionDialogInitialize()`
2. [Set parameters for the player selection dialog](basic-procedure.html#player-selection-dialog-library-overview_1_2__li_skc_wmj_gbc): `scePlayerSelectionDialogParamInitialize()`, `ScePlayerSelectionDialogParam`
3. [Display the player selection dialog](basic-procedure.html#player-selection-dialog-library-overview_1_2__li_xxw_vnj_gbc): `scePlayerSelectionDialogOpen()`
4. [Get the result of calling the player selection dialog](basic-procedure.html#player-selection-dialog-library-overview_1_2__li_hvd_vnj_gbc): `scePlayerSelectionDialogGetResult()`, `ScePlayerSelectionDialogResult`
5. [Terminate the player selection dialog](basic-procedure.html#player-selection-dialog-library-overview_1_2__li_r5r_5nj_gbc): `scePlayerSelectionDialogTerminate()`

Figure 1. Basic Procedure

1. **Initialize the player selection dialog**

   Call `scePlayerSelectionDialogInitialize()` and initialize the player selection dialog.

   ```
   if (scePlayerSelectionDialogInitialize () < 0 ) {
       // Error handling
   }
   ```
2. **Set parameters for the player selection dialog**

   Prepare an `ScePlayerSelectionDialogParam` structure and initialize with `scePlayerSelectionDialogParamInitialize()`. After initialization, set the maximum number of players who can be selected, the list of players' initial states, and other parameters. The following example is specified such that the title is set to "Select Player", the number of players who can be selected is set to 8, and blocked users are displayed as non-selectable.

   ```
   ScePlayerSelectionDialogParam param;
   scePlayerSelectionDialogParamInitialize( &param );

   param.userId = userId;// Obtain in advance
   param.maxSelectable = 8;
   strncpy(param.dialogTitle, "Select Player",
    SCE_PLAYER_SELECTION_DIALOG_MAX_TITLE_SIZE);
   param.behaviorOptions = 
   SCE_PLAYER_SELECTION_DIALOG_BEHAVIOR_OPTION_DISABLE_BLOCKED_PLAYER;
   ```

   For parameter details, see [PlayerSelectionDialog Library Reference](../PlayerSelectionDialog-Reference/__document_toc.html).
3. **Display the player selection dialog**

   Call `scePlayerSelectionDialogOpen()` with the parameters set in [2](basic-procedure.html#player-selection-dialog-library-overview_1_2__li_skc_wmj_gbc) as an argument. The player selection dialog showing a friend list of the user specified in `param.userId` will be displayed, and it will become possible to receive user operation.

   ```
   if (scePlayerSelectionDialogOpen( &param ) < 0 ) {
       // Error handling
   }
   ```

   After `scePlayerSelectionDialogOpen()` terminates normally, call `scePlayerSelectionDialogUpdateStatus()` at regular intervals (such as at every rendering frame) to poll the operation status of the dialog.

   ```
   while(1) {
       stat = scePlayerSelectionDialogUpdateStatus();
       if( stat == SCE_COMMON_DIALOG_STATUS_FINISHED ) {
           break;
       } else if( stat == SCE_COMMON_DIALOG_STATUS_RUNNING ) {
           if( need_close ) {
               scePlayerSelectionDialogClose();
               break;
           }
       }
       sceKernelUsleep(16666);
   }
   ```

   `SCE_COMMON_DIALOG_STATUS_RUNNING` will return for the operation status while dialog is being displayed, therefore wait until the dialog is closed and the operation status becomes `SCE_COMMON_DIALOG_STATUS_FINISHED`.
4. **Get the result of calling the player selection dialog**

   When the operation status transitions to `SCE_COMMON_DIALOG_STATUS_FINISHED`, obtain the call result with `scePlayerSelectionDialogGetResult()`.

   ```
   ScePlayerSelectionDialogResult result;
   memset( &result, 0, sizeof(result) );
   if( scePlayerSelectionDialogGetResult( &result ) < 0 ) {
       // Error handling
   }
   ```

   To display the player selection dialog again after obtaining the call result, return to step [2](basic-procedure.html#player-selection-dialog-library-overview_1_2__li_skc_wmj_gbc) and start again from setting the parameters.
5. **Terminate the player selection dialog**

   Once you obtain the call result and no longer require the player selection dialog, call `scePlayerSelectionDialogTerminate()` to perform termination processing. This will free the resources allocated upon initialization and the operation status will transition to `SCE_COMMON_DIALOG_STATUS_NONE`.

   Note:

   `scePlayerSelectionDialogOpen()` can also be called when the operation status is `SCE_COMMON_DIALOG_STATUS_FINISHED`. Thus, it is possible to display the dialog again without having to first execute `scePlayerSelectionDialogTerminate()` and terminate the player selection dialog.

## Close the Player Selection Dialog by the Application

Call `scePlayerSelectionDialogClose()` to close the player selection dialog without waiting for user operation. When the call of this function succeeds and `scePlayerSelectionDialogUpdateStatus()` is periodically called thereafter, the dialog will carry out processing to close the dialog display; the operation status will transition to `SCE_COMMON_DIALOG_STATUS_FINISHED` upon processing completion.

When the dialog is closed with `scePlayerSelectionDialogClose()`, the dialog call result that can be obtained with `scePlayerSelectionDialogGetResult()` will be `SCE_COMMON_DIALOG_RESULT_OK`.

## Abort Processing

Call `scePlayerSelectionDialogTerminate()` to quickly abort player selection dialog processing by the application. Processing will be immediately terminated and the operation status will transition to `SCE_COMMON_DIALOG_STATUS_NONE`.

## Handling of Unexpected Fatal Errors

There is a possibility that the following functions will return `SCE_COMMON_DIALOG_ERROR_UNEXPECTED_FATAL`. In such cases, call `scePlayerSelectionDialogTerminate()`. Afterward, re-execute the processes starting with step [1](basic-procedure.html#player-selection-dialog-library-overview_1_2__li_dq3_mnj_gbc).

* `scePlayerSelectionDialogInitialize()`
* `scePlayerSelectionDialogOpen()`
* `scePlayerSelectionDialogGetResult()`