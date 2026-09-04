# SigninDialog Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/SigninDialog-Overview/using-the-library.html

# Using the Library

# Display the Signin Dialog

The signin dialog is displayed as shown in the figure below. It can be closed by user operation.

Signin Dialog

The signin dialog is not a common dialog that is implemented using the CommonDialog library. Therefore, it is technically possible to call a common dialog while the signin dialog is being displayed. In such cases, however, the signin dialog will be the frontmost dialog displayed, preventing the common dialog from being visible to the user.

# Use Cases for Signin Dialog

The signin dialog can be used to prevent errors that occur due to a user not being in the signed-in state for PlayStation™Network.

For example, consider a case where an API that uses the PlayStation™Network features must be called in the middle of gameplay. An error will occur if the user is in the signed-out state at the time of the call, but if asking the user to sign in again could have serious effects on their game experience, it will be possible to implement preventative measures such as calling the signin dialog at a location where effects on the gameplay experience can be minimalized (during gameplay preparations, etc.).

## Signed-in State and Network Connection States

The "signed-in state" on the PlayStation®5 platform is a status that indicates that the services provided by PlayStation™Network can be used by a user. Upon successful user verification, the user will enter the signed-in state, and the signed-in state will be hereafter retained even if network disconnection occurs or the PlayStation®5 is restarted.

The SigninDialog library only provides a feature for users to enter the signed-in state to PlayStation™Network, it is not related to network connection states. Therefore, a user is guaranteed to be in the signed-in state when the signin dialog call result obtained with `sceSigninDialogGetResult()` is `SCE_SIGNIN_DIALOG_RESULT_OK`, but the PlayStation®5 being connected to a network is not guaranteed.

For details on the signed-in state, refer to the "Sign-in States" chapter in the [Np Library Overview](../Np-Overview/__document_toc.html) document.

## Signin Dialog Call Conditions

Regardless of whether a user is in the signed-in state or not, calling the signin dialog will not have any negative effects. If a user is already in the signed-in state, the signin dialog will terminate immediately without displaying anything on the screen, and a call result equivalent to "OK" will be obtained.

In addition, regardless of whether a network connection has been established or not, calling the signin dialog will not have any negative effects. When a user is in the signed-out state, access to servers of PlayStation™Network occur for sign-in processing, but the signin dialog will display an appropriate error message if network access fails at such times. Furthermore, when the signin dialog terminates in such a state, a call result equivalent to the user cancelling the dialog will be obtained.

## Ex-post Measures Using the ErrorDialog Library

Even after the signin dialog is called, it is still possible that errors will occur. Network disconnection or sign out can occur at any time, therefore ex-post measures must be implemented for cases where an error is returned by an API that uses the PlayStation™Network features, even after calling the signin dialog in advance. Since the ErrorDialog library can respond to various error causes including sign out, using this library is recommended for ex-post measures. For details, refer to the [Np Library Overview](../Np-Overview/__document_toc.html) document and the [ErrorDialog Library Overview](../ErrorDialog-Overview/__document_toc.html) document.

# Basic Procedure

This section explains the procedure to display the signin dialog using the SigninDialog library. The processing flow is summarized as follows.

1. [Initialize the signin dialog](basic-procedure.html#signin-dialog-library-overview_1_3__basic_procedure_1)
2. [Set parameters for the signin dialog](basic-procedure.html#signin-dialog-library-overview_1_3__basic_procedure_2)
3. [Display the signin dialog](basic-procedure.html#signin-dialog-library-overview_1_3__basic_procedure_3)
4. [Monitor the signin dialog status](basic-procedure.html#signin-dialog-library-overview_1_3__basic_procedure_4)
5. [Terminate the signin dialog](basic-procedure.html#signin-dialog-library-overview_1_3__basic_procedure_5)

The application process flow and SigninDialog library operations status transitions are shown in the following.

Basic Procedure and Operation Status Transitions

1. **Initialize the signin dialog**

   Call `sceSigninDialogInitialize()` and initialize the signin dialog.

   ```
   if (sceSigninDialogInitialize() < 0 ) {
   	// Error handling
   }
   ```
2. **Set parameters for the signin dialog**

   Prepare a `SceSigninDialogParam` structure as a signin dialog call parameter and initialize the structure with `sceSigninDialogParamInitialize()`. Afterward, specify the user ID of the user to be signed-in as a parameter required for the signin dialog. User IDs can be obtained from the UserService library, etc.

   ```
   SceSigninDialogParam param;
   sceSigninDialogParamInitialize( &param );
   int32_t ret = sceUserServiceGetInitialUser( &param.userId );
   if ( ret != SCE_OK ) {
   	// Error handling
   	return;
   }
   ```
3. **Display the signin dialog**

   Call `sceSigninDialogOpen()` with the dialog call parameters set above as an argument. The signin dialog will be displayed and the application will make a transition to a background state.

   ```
   if (sceSigninDialogOpen( &param ) < 0 ) {
   	// Error handling
   }
   ```
4. **Monitor the signin dialog status**

   Call `sceSigninDialogUpdateStatus()` at regular intervals (such as at every rendering frame) to poll the operation status of the signin dialog.

   ```
   while(1) {
   	stat = sceSigninDialogUpdateStatus();
   	if( stat == SCE_SIGNIN_DIALOG_STATUS_FINISHED ) {
   		break;
   	} else if( stat == SCE_SIGNIN_DIALOG_STATUS_RUNNING ) {
   		if( need_close ) {
   			sceSigninDialogClose();
   			break;
   		}
   	}
   }
   ```

   Because `sceSigninDialogUpdateStatus()` realizes communication between the system software and the process, it entails a certain overhead. A more lightweight function, `sceSigninDialogGetStatus()`, is provided to obtain the operation status without updating it first; this function can be used to confirm the status from a different thread that the one updating the status within the same frame.

   `SCE_SIGNIN_DIALOG_STATUS_RUNNING` will return for the operation status while dialog is being displayed, therefore wait until the dialog is closed with a user operation, etc. and the operation status becomes `SCE_SIGNIN_DIALOG_STATUS_FINISHED`.
5. **Terminate the signin dialog**

   After confirming that the signin dialog has been closed and the operation status became `SCE_SIGNIN_DIALOG_STATUS_FINISHED`, call `sceSigninDialogTerminate()` to terminate the dialog. This will free the resources allocated upon initialization and the operation status will transition to `SCE_SIGNIN_DIALOG_STATUS_NONE`.

   Note:

   `sceSigninDialogOpen()` can also be called when the operation status is `SCE_SIGNIN_DIALOG_STATUS_FINISHED`. Thus, the application can display the signin dialog again without executing `sceSigninDialogTerminate()` and terminating the signin dialog first.

## Close the Signin Dialog by the Application

Call `sceSigninDialogClose()` to close the signin dialog without user operation. When the call of this function succeeds, the signin dialog will start processing to close dialog display; the operation status will transition to `SCE_SIGNIN_DIALOG_STATUS_FINISHED` upon processing completion.

## Abort Processing

Call `sceSigninDialogTerminate()` to quickly abort signin dialog processing by the application. Display can be terminated faster by calling this function rather than `sceSigninDialogClose()` and the operation status will immediately transition to `SCE_SIGNIN_DIALOG_STATUS_NONE`.

## API Summary

The APIs used in basic processing to display the signin dialog are shown below.

APIs Used in Basic Processing

| **API** | **Description** |
| --- | --- |
| `sceSigninDialogInitialize()` | Function that initializes the signin dialog |
| `SceSigninDialogParam` | Parameter structure for the signin dialog |
| `sceSigninDialogParamInitialize()` | Function that initializes the parameter structure |
| `sceSigninDialogOpen()` | Function that displays the signin dialog |
| `sceSigninDialogUpdateStatus()` | Function to update the signin dialog operation status and to obtain the latest status |
| `sceSigninDialogGetStatus()` | Function that gets the operation status |
| `sceSigninDialogClose()` | Function that closes the signin dialog |
| `sceSigninDialogTerminate()` | Function that terminates the signin dialog |