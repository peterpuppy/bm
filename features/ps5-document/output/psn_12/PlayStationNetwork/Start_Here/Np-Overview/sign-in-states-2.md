# Np Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Np-Overview/sign-in-states-2.html

# Sign-in States

# Sign-in States

A sign-in state whether or not a user can use the PlayStation™Network services. Two sign-in states are defined: PlayStation™Network services cannot be used at all in the "signed-out" state, and services can be used in the "signed-in" state.

## Signed-out

Signed-out refers to a state in which no connection can be made to PlayStation™Network regardless of whether a network connection is available or not. This state is reached when the user has not set an account (when the user has not signed up, for example), when some fatal error (a password mismatch, for example) is generated or when the user has explicitly prohibited sign-in from the system software menu.

Most of PlayStation™Network functionalities become unusable in the signed-out state. To switch to the signed-in state, the user must perform the sign-in operation (or the sign-up operation) in the system software menu. Therefore, network connection is required to switch to the signed-in state from the signed-out state.

## Signed-in

Signed-in refers to a state in which connection to PlayStation™Network is possible as long as network conditions are satisfied.

This state is reached when the user successfully completes signup, or successfully completes sign-in operation from the system software menu. Even if the network subsequently becomes disconnected or the console is restarted, the signed-in state will be maintained.

## Transitioning from a Signed-in State to a Signed-Out State

After a user transitions to a signed-in state, they may transition to a signed-out state. The main causes of transitioning to a signed-out state are shown in the following.

* A sign-out error is returned from the server for invalid authentication information, etc. during communication between the server and the system software or an application
* The user performed the sign-out operation

# Obtaining/Monitoring the Signed-in State

The Np library provides the following functionalities regarding the signed-in state.

* Obtaining the current signed-in state
* Receiving notifications regarding changes in the signed-in state

# Causing Transitions to the Signed-in State

In order to cause a transition to the signed-in state for a user in the signed-out state in an application, it is possible to use the ErrorDialog library and it is possible to use the SigninDialog library.

When a function that uses PlayStation™Network is called for a user who is not in the signed-in state, an error will return. Call the ErrorDialog library with the error code at this time as an argument, then the ErrorDialog library will display an appropriate error message according to the error code, and the user will be prompted to sign in as required.

In addition to signed-out states, the ErrorDialog library is designed to display appropriate messages for a variety of error codes including for cases where PlayStation™Network cannot be used for other reasons, therefore it is recommended that the ErrorDialog library is used regularly.

In cases where it is known that the user is in the signed-out state such as when the application uses `sceNpGetState()`, etc., and it is desired to prompt sign-in without going through an error screen, it is also possible to directly call the sign-in screen using the SigninDialog library. Note that the SigninDialog library can cause users to become signed in, but it is not guaranteed that usage of PlayStation™Network in applications will be possible. For details, refer to the [SigninDialog Library Overview](../SigninDialog-Overview/__document_toc.html) document.