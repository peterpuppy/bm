# LoginDialog Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/LoginDialog-Overview/using-the-library.html

# Using the Library

# Display the Login Dialog

The login dialog is displayed as shown in the figure below. It can be closed by user operation.

Login Dialog

The login dialog is not a common dialog that is implemented using the CommonDialog library. Therefore, it is technically possible to call a common dialog while the login dialog is being displayed. In such cases, however, the login dialog will be the frontmost dialog displayed, preventing the common dialog from being visible to the user.

# Login Dialog Operation Modes

The following shows the two operation modes are available for login dialog, as well as the characteristics and purposes of each mode. Select a mode according to application purpose then display login dialog.

## Mode Where Only User Not Logged In Can Be Selected

In this mode, the login dialog will display a user list in a state where only users not logged in to the PlayStation®5 can be selected. When a user is selected in the login dialog, the LoginDialog library will cause the selected user to log in, and the ID of the user will return to the caller application as a dialog call result upon dialog termination.

This mode is intended to be used in cases where applications independently implement selection processing for logged in users. A list of logged in users can be obtained with the UserService library.

## Mode Where All Users Registered on the PlayStation®5 Can Be Selected

In this mode, the login dialog will display a list of all selectable users that are registered on the PlayStation®5, regardless of whether they are logged in or not.

When a user is selected in login dialog, the LoginDialog library will not do anything if the user is already logged in, and the LoginDialog library will log in a user to the PlayStation®5 if they are not already logged in, then the ID of the user will return to the caller application as a dialog call result when the dialog terminates. Through this, the selected user is guaranteed to be logged in upon normal termination of the login dialog.

In this mode, it is possible to exclude specific users from lists of selectable users.

In situations such as when selecting Player 2 in a 2-player game when Player 1 has already been confirmed, it will be possible to exclude the user confirmed as Player 1 from the selections in advance.

# Basic Procedure

This section explains the procedure to display the login dialog using the LoginDialog library. The processing flow is summarized as follows.

1. [Initialize the login dialog](basic-procedure.html#login-dialog-library-overview_1_3__basic_procedure_1)
2. [Set parameters for the login dialog](basic-procedure.html#login-dialog-library-overview_1_3__basic_procedure_2)
3. [Display the login dialog](basic-procedure.html#login-dialog-library-overview_1_3__basic_procedure_3)
4. [Terminate the login dialog](basic-procedure.html#login-dialog-library-overview_1_3__basic_procedure_4)

The application process flow and LoginDialog library operations status transitions are shown below.

Basic Procedure and Operation Status Transitions

1. **Initialize the login dialog**

   Call `sceLoginDialogInitialize()` and initialize the login dialog.

   ```
   if (sceLoginDialogInitialize() < 0 ) {
   	// Error handling
   }
   ```
2. **Set parameters for the login dialog**

   Prepare a `SceLoginDialogParam` type structure as a login dialog call parameter and initialize the structure with `sceLoginDialogParamInitialize()`. Afterward, specify the operation mode as the parameters required for the login dialog. At this time, it is also possible to specify users to exclude from selections for users to log in or log out. User IDs can be obtained with the UserService library, etc.

   ```
   SceLoginDialogParam param;
   sceLoginDialogParamInitialize( &param );
   param.mode = SCE_LOGIN_DIALOG_MODE_ALL_USERS;

   SceUserServiceUserId userOfMainCharacter;
   int32_t ret = sceUserServiceGetInitialUser( &userOfMainCharacter );
   if ( ret != SCE_OK ) {
   	// Error handling
   	return;
   }
   param.excludeUsersFromLoginList[0] = userOfMainCharacter;
   param.excludeUsersFromLogoutList[0] = userOfMainCharacter;
   ```
3. **Display the login dialog**

   Call `sceLoginDialogOpen()` with the dialog call parameters set above as an argument. The login dialog will be displayed, it will become possible to receive user operation, and the application will make a transition to a background state.

   ```
   if (sceLoginDialogOpen( &param ) < 0 ) {
   	// Error handling
   }
   ```

   After `sceLoginDialogOpen()` terminates normally, call `sceLoginDialogUpdateStatus()` at regular intervals (such as at every rendering frame) to poll the operation status of the login dialog.

   ```
   while(1) {
   	stat = sceLoginDialogUpdateStatus();
   	if( stat == SCE_LOGIN_DIALOG_STATUS_FINISHED ) {
   		break;
   	} else if( stat == SCE_LOGIN_DIALOG_STATUS_RUNNING ) {
   		if( need_close ) {
   			sceLoginDialogClose();
   			break;
   		}
   	}
   }
   ```

   Because `sceLoginDialogUpdateStatus()` realizes communication between the system software and the process, it entails a certain overhead. A more lightweight function, `sceLoginDialogGetStatus()`, is provided to obtain the operation status without updating it first; this function can be used to confirm the status from a different thread that the one updating the status within the same frame.

   `SCE_LOGIN_DIALOG_STATUS_RUNNING` returns while the login dialog is being displayed. Wait until the dialog is closed and the operation status becomes `SCE_LOGIN_DIALOG_STATUS_FINISHED`. In addition, the application will make a transition to the foreground state.
4. **Terminate the login dialog**

   After confirming that the login dialog has been closed and the operation status became `SCE_LOGIN_DIALOG_STATUS_FINISHED`, call `sceLoginDialogTerminate()` to terminate the dialog. This will free the resources allocated upon initialization and the operation status will transition to `SCE_LOGIN_DIALOG_STATUS_NONE`.

   Note:

   `sceLoginDialogOpen()` can also be called when the operation status is `SCE_LOGIN_DIALOG_STATUS_FINISHED`. Thus, the application can display the login dialog again without executing `sceLoginDialogTerminate()` and terminating the login dialog first.

## Close the Login Dialog by the Application

Call `sceLoginDialogClose()` to close the login dialog without user operation. When the call of this function succeeds, the login dialog will start processing to close dialog display; the operation status will transition to `SCE_LOGIN_DIALOG_STATUS_FINISHED` upon processing completion.

## Abort Processing

Call `sceLoginDialogTerminate()` to quickly abort login dialog processing by the application. Display can be terminated faster by calling this function rather than `sceLoginDialogClose()` and the operation status will immediately transition to `SCE_LOGIN_DIALOG_STATUS_NONE`.

## API Summary

The API features used in basic processing to display the login dialog are shown below.

API Features Used in Basic Processing

| **API Feature** | **Description** |
| --- | --- |
| `sceLoginDialogInitialize()` | Function that initializes the login dialog |
| `SceLoginDialogParam` | Parameter structure for the login dialog |
| `sceLoginDialogParamInitialize()` | Function that initializes the parameter structure |
| `sceLoginDialogOpen()` | Function that displays the login dialog |
| `sceLoginDialogUpdateStatus()` | Function to update the login dialog operation status and to obtain the latest status |
| `sceLoginDialogGetStatus()` | Function that gets the operation status |
| `sceLoginDialogClose()` | Function that closes the login dialog |
| `sceLoginDialogTerminate()` | Function that terminates the login dialog |