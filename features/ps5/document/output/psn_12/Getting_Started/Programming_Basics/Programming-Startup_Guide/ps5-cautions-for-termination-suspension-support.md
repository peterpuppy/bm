# Programming Startup Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Programming-Startup_Guide/ps5-cautions-for-termination-suspension-support.html

# Application State Transitions

This topic explains application state transitions. It lists points to note concerning foreground execution, background execution, termination preparation, various suspended states, and state transitions.

# Application States

After an application starts, it will be in one of the following states:

* Foreground execution
* Background execution
* Termination preparation
* Suspended

Application State Transitions

# Foreground Execution

The first transition after an application starts is the foreground execution state. When a user performs the following procedure during foreground execution, the application will transition to the background execution state. (The following is one procedural example.)

1. Press the PS button.
2. Select "Home" from the menu that is displayed as an overlay

# Background Execution

When a user performs the following procedure during background execution, the application will transition to the foreground execution state. (The following is one procedural example.)

1. Press the PS button.
2. Select the option to relaunch a recently launched application from the menu that is displayed as an overlay
3. Select the application

During background execution, the application screen will not be displayed, and only the system software screen will be displayed. In addition, application audio will not be output. Applications can obtain whether it is in the background state using `sceSystemServiceGetStatus()`. For details, refer to [SystemService Library Overview - Using the Library - Obtaining the Execution Status of an Application](../SystemService-Overview/obtaining-the-execution-status-of-an-application.html).

Note that the use of the following resources will be limited during background execution:

* CPU (Refer to [Kernel Overview - CPU Management](../Kernel-Overview/cpu-management.html) for details.)
* SSD (There is currently no difference between foreground and background execution.)
* GPU (Refer to the "[Resources That Can Be Used by Applications](resources-that-can-be-used-by-applications.html "This topic explains the various resources that can be used by applications. It provides the quantities that can be used for CPUs, GPUs, memory, file descriptors, threads, and event queues. Be aware that what is described here are specifications that are reinforced for development on DevKits and may differ from the specifications for TestKits and retail units.")" chapter for details about the restriction.)

# Termination Preparation

When a user performs the following procedure, the application will transition to the termination preparation state, and then the system will immediately terminate the application.

1. Press the PS button.
2. Select "Power" > "Turn Off PS5" from the menu that is displayed as an overlay

In terms of the internal processing of the system software, transition to the termination preparation state is the same as the transition to the suspended state.

It is not possible for applications to detect termination.

# Suspended

The main conditions for application transitions to the suspended state are as follows.

* An application with the InitialUserAlwaysLoggedIn parameter enabled in param.json:

  When the user who started the application logs out, the application will transition to the suspended state. Only the user who started the application can resume application operation.
* An application with the InitialUserAlwaysLoggedIn parameter disabled in param.json:

  When all users log out, the application will transition to the suspended state. Any user can resume application operation. After the transition to the suspended state, the application will transition to the foreground state and resume operation when a user turns the power on again. It is not possible for applications to detect transitions to the suspended state, but resuming from the suspended state can be detected by obtaining resume events using `sceSystemServiceReceiveEvent()`.

# Suspension Operations During Development

If an application implements a feature to perform some kind of processing when operation is resumed by obtaining resume events, causing a transition to the suspended state is required in order to test such features. By setting [★Debug Settings] > [Game] > [Instant App Suspending] in the system software to "On", performing the following procedure during foreground execution will cause a transition to the suspended state rather than the background state.

1. Press the PS button.
2. Select "Home" from the menu that is displayed as an overlay

# Cautions for Termination/Suspension Support

The application should take into consideration the points below in order to properly perform application termination and suspension.

## Save Data

When the application is suspended, if save data is being updated, the suspension of the application is suppressed until the update is completed. However, because suppressing suspension for a long time has a negative impact on the user experience, the system will make the application crash after a certain time passes and force it to terminate. To prevent this, ensure that updating save data completes as quickly as possible, referring to "Save Data Update Modes", "Save Data Update Periods", and "Write Processing in Consideration of the Update Period" in the [SaveData Library Overview](../SaveData-Overview/__document_toc.html) document.

## Required Processing Regarding Graphics

`sce::Agc::suspendPoint()` must be called periodically in the Agc library to ensure suspension of the graphics pipe. For details, refer to the relevant technical note (<https://game.develop.playstation.net/technotes/view/100>).

# System Suspend/Resume Feature

The system suspend/resume feature transitions the system software to rest mode and eventually resumes it while keeping an application in a suspended state throughout. When user operation causes the system to be suspended, the system will cause applications to make transitions to suspended states, and the applications will resume after the system resumes.

## Supporting the System Suspend/Resume Feature

Applications do not need to add any special processing in order to support the system suspend/resume feature. However, the following are more important than ever in implementations because serious problems will occur if inappropriate processing is being performed.

**Support for network disconnection:**

System suspension/resumption will cause network disconnection. This is the same phenomenon as when the network cable is disconnected, but note that the rate of occurrence will be higher. If the network is disconnected, the IP address will be released. When this happens, sockets already created may not be able to continue processing, depending on the situation, and will return `SCE_NET_EINACTIVEDISABLED`. (For details, refer to [Net Library Overview - Notes - Operation Upon IP Address Release](../Net-Overview/operation-upon-ip-address-release.html).)

When resumed, it is necessary to display an error message indicating that the network was disconnected.

Use one of the procedures below to test how the application responds to network disconnection. (It is also possible to use the "System Suspend/Resume Operations" mentioned later.)

* When testing using the system software
  1. Press the PS button.
  2. Set "Network" "Network Settings" > "Settings" > "Connect to Internet" to off.
  3. Return to the application.
* When testing using Target Settings for PlayStation®5
  1. Set "Network" > "Connect to Internet" to off.
  2. Click "Apply"

**Time:**

Time will continue to advance during system suspension/resumption. If an application repeatedly obtains time, note that there may be a significant gap with a previously obtained value. Depending on the usage, use the "process time" that stops during system suspension/resumption. For details, refer to [Kernel Overview - Time Management](../Kernel-Overview/time-management.html).

**GPU timestamp value:**

If GPU timestamp values are obtained before and after `suspendPoint()`, the two timestamp values may be far apart, or the large and small values may be reversed (due to resetting of the timestamp counter). This occurs when the application is suspended and resumed, but note that the values may be particularly far apart when a system suspend/resume occurs.

Implement your application in such a manner that a call of `suspendPoint()` essentially never falls within the range when timestamp values are compared. If it is unavoidable to obtain and compare timestamps spanning a call of `suspendPoint()`, implement appropriate measures to be performed if the difference between the values is extremely large or if the latter value is smaller (such as discarding the comparison result without using it)

## Reference: System Suspend/Resume Operations

It is possible to transfer from the powered-on state to system suspend state by pressing the power button on the front of the DevKit.

System suspend/resume is also possible from the host PC by performing the following operations.

* Performing system suspend by operating the system software:
  1. Press the PS button.
  2. Select "Power" > "Enter Rest Mode" in the displayed Control Center
* Performing system suspend by operating the host PC:

  A target can be transferred from the powered-on state to the system suspend state with Target Manager or `prospero-ctrl power rest-mode`.
* Performing system resume by operating the host PC:

  A target can be transferred from the system suspend state to the powered-on state with Target Manager or `prospero-ctrl power on`.