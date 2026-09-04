# Matchmaking Overview – WebAPI 1

Source: https://game.develop.playstation.net/resources/documents/WebAPI/1/Matchmaking-Overview/how-push-events-are-received.html

# Push Events

The Push events that occur with the Matchmaking Web API are as follows:

List of Push Events Relating to Matchmaking

| **Datatype** | **API Feature that Can Cause or Trigger the Push Event** | **Destination** |
| --- | --- | --- |
| `psn:matchmaking:ticket:submitted` | A matchmaking ticket was created   * `submitTicket` | All members of the matchmaking ticket |
| `psn:matchmaking:ticket:canceled` | The matchmaking ticket was canceled   * `cancelTicket` * `submitTicket` | All members of the matchmaking ticket |
| `psn:matchmaking:ticket:timedOut` | Matchmaking could not be achieved within the amount of time set in the ruleset   * `submitTicket` | All members of the matchmaking ticket |
| `psn:matchmaking:ticket:failed` | A system error of some kind occurred after placement of the ticket in the matchmaking ticket pool   * `submitTicket` | All members of the matchmaking ticket |
| `psn:matchmaking:offer:failed` | A system error occurred upon creating a Game Session after a matchmaking offer was processed. (Details of the error can be checked by issuing getOffer.)   * `submitTicket` | All members included in the matchmaking offer |
| `psn:sessionManager:gs:invitations:created` | Matchmaking has been achieved and a reservation to join the Game Session has been made   * Matchmaking is achieved | Members for whom a reservation to join has been made |
| `psn:sessionManager:gs:matchmaking:updated` | Information relating to Game Session matchmaking (offer ID) has been updated   * Backfilling matchmaking has been achieved | Participating members of the backfilling-target Game Session |

# How Push Events Are Received

For details on how applications receive Push events, refer to the explanation in the [PlayStation™Network Web APIs Overview](../../../SDK/latest/PSN_WebAPI-Overview/__document_toc.html) document.