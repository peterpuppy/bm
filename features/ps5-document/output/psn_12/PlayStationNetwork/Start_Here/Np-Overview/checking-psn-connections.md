# Np Library Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Np-Overview/checking-psn-connections.html

# Checking PlayStation™Network Connections

# Checking the PlayStation™Network Reachability State

The connection states when PlayStation™Network is being used on PlayStation®5 requires various state management such as the network state (IP address obtainment state/LAN connection state), sign-in state, and state of real-time connection to servers of PlayStation™Network. In order to handle these connection states at once, they will be defined as PlayStation™Network reachability states.

## PlayStation™Network Reachability States

The following three states are defined as PlayStation™Network reachability states.

* Unavailable (`SCE_NP_REACHABILITY_STATE_UNAVAILABLE`)
* Available (`SCE_NP_REACHABILITY_STATE_AVAILABLE`)
* Reachable (`SCE_NP_REACHABILITY_STATE_REACHABLE`)

**Unavailable (SCE\_NP\_REACHABILITY\_STATE\_UNAVAILABLE)**

In this state, PlayStation™Network features cannot be used, or the reachability has not yet been checked. This state will occur when a network cannot be used because an IP address has not been obtained, etc., or when PlayStation™Network cannot be used (when sign-out occurs, etc.).

**Available (SCE\_NP\_REACHABILITY\_STATE\_AVAILABLE)**

In this state, it has been confirmed that PlayStation™Network features can be used, but connectivity to PlayStation™Network has not been maintained. There is a possibility of a temporary disconnection due to reasons such as WAN disconnection.

**Reachable (SCE\_NP\_REACHABILITY\_STATE\_REACHABLE)**

In this state, PlayStation™Network features can be used, and a real-time connection to servers of PlayStation™Network has been established.

## Monitoring the PlayStation™Network Reachability State

By calling `sceNpGetNpReachabilityState()`, applications can query the system software to obtain whether PlayStation™Network is reachable. The system software continues to check the PlayStation™Network reachability state while a user is signed in; therefore, in principle, the state will automatically be "Reachable (`SCE_NP_REACHABILITY_STATE_REACHABLE`)".

When `sceNpCheckNpReachability()` is called, applications can explicitly check the reachability state. For example, this should be used in situations where a continuous online connection (i.e., including WAN connectivity) is needed, such as when making a transition to online multiplayer gameplay, when using real-time messages that use the NpSessionSignaling library, or when using push notifications. In such cases, after calling `sceNpCheckNpReachability()` to confirm that a reachable state exists, monitor the state with `sceNpGetNpReachabilityState()` or `SceNpReachabilityStateCallback`. (Avoid calling `sceNpCheckNpReachability()` at regular intervals.) When the state is a state other than `SCE_NP_REACHABILITY_STATE_REACHABLE`, it means that the continuous connection with PlayStation™Network has been lost for one of various reasons such as WAN disconnection, so perform countermeasures, such as suspending use of the online multiplayer feature.

Nevertheless, request/response-type network processing is performed for most access to PlayStation™Network, such as accessing data on PlayStation™Network (Title Cloud Storage Web API or Leaderboards Web API) or accessing PlayStation™Store using the In-Game Catalog Web API; therefore, it is not necessary to use `sceNpCheckNpReachability()` for those access cases. Since user convenience might be negatively affected, do not needlessly monitor the reachability state in such situations.

## PlayStation™Network Reachability State Disconnection Detection

While a user is signed in, the system software continues to check the PlayStation™Network reachability state. However, it takes a certain amount of time after the console experiences a WAN disconnection before the system determines that a reachable state has been lost. During this period, the system software withholds its determination that a WAN-side disconnection has occurred and waits for the connection to be restored. If the connection is restored after a short amount of time, the system software continues to consider the console to be in a reachable state.

Thus, functions that monitor reachability states behave as though the system is in a reachable state (`SCE_NP_REACHABILITY_STATE_REACHABLE`) for a certain amount of time immediately following a WAN disconnection. The monitored results transition from the reachable state (`SCE_NP_REACHABILITY_STATE_REACHABLE`) to another state if the WAN connection is not restored even after some time elapses.