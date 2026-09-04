# Trophy System Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Trophy_System-Overview/appendix-a-configuration-changes-that-can-be-made-based-on-t.html

# Appendix A: Configuration Changes That Can Be Made Based on the NP Config Tag State

Configuration Changes That Can Be Made Based on the NP Config Tag State

| **Target** | **Operation** | **NP Config Tag State** | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| In Development | Tagged | In Format QA | Format QA Completed | In Production |
| Trophy Sets | Modifying | Yes | No | No | No | No |
| Trophy Groups | Deleting | Yes | No | No | No | No |
| Modifying | Yes | No | No | No | No |
| Trophies | Deleting | Yes | No | No | No | No |
| Modifying | Yes | No | No | No | No |

Modifiability of Trophy Set Attributes while In Development

| **Attribute** | **Modifiable** | **Note** |
| --- | --- | --- |
| Default Language | No |  |
| Trophy Set Name | Yes |  |
| Trophy Set Icon Image | Yes |  |

Modifiability of Trophy Group Attributes while In Development

| **Attribute** | **Modifiable** | **Note** |
| --- | --- | --- |
| Trophy Group ID | No |  |
| Trophy Group Number | No |  |
| Trophy Group Name | Yes |  |
| Trophy Group Icon Name | Yes |  |

Modifiability of Trophy Object Attributes while In Development

| **Attribute** | **Modifiable** | **Note** |
| --- | --- | --- |
| Object ID | No |  |
| Group | No |  |
| Trophy ID | No | Assigned automatically |
| Display Order | Yes |  |
| Display Name | Yes |  |
| Description | Yes |  |
| Trophy Grade | Yes |  |
| Linked Platinum Trophy | Yes | Only the ID of a platinum trophy can be specified |
| Has Rewards | Yes |  |
| Reward Name | Yes |  |
| Reward Image | Yes |  |
| Hidden | Yes |  |
| Trophy Icon Image | Yes |  |
| Unlock Style | No |  |
| Trophy Unlock Condition | Yes |  |