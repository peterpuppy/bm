# Universal Data System Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Universal_Data_System-Guide/reviewing-operational-history.html

# Operational History

The operational history tracks the creation, update, and deletion of
PlayStation™Network objects, UDS events, and trophies.

Use **Operational History** to view the operational history for the currently selected
NP Communication ID, shown in the following figure. The operational history related to
stats definitions and extractions are currently not tracked.

Operational History

# Operational History

This chapter describes viewing the operational history of the UDS Management
Tool.

The UDS Management Tool tracks the creation, update, and deletion of the following
entities:

* PSN objects
* UDS events
* Trophies
* NP Config Tags
* NP Communication ID metadata

Operational history also tracks the following bulk activities:

* PlayStation™Network object bulk import
* UDS event bulk import
* Trophy bulk import
* Tournament bulk import
* UBP import

The operational history related to stats definitions and extractions are not tracked.

## User Permissions and Limitations

If you are a "Viewer", "Editor", or "Owner" title collaborator, you can view all operational history.

# Reviewing Operational History

This topic covers the procedure for reviewing operational history for NP Communication IDs.

To review the operational history for currently selected NP Communication ID, click
the **Operational History** tab. The operational history view page is displayed as shown in the following figure.
Select the **Load More** button to display more records. You can search the record by specifying Actor. You
can also filter the records by date time range, log level, action, target, and group
ID.

Operational History

# Audit Log Grouping

If one or more entity updates are triggered by a bulk action, these entries can be
displayed in a group. All related audit log entries have the same group ID value in
the audit log property.

For example, if two PlayStation™Network objects are created by bulk object import, all four audit log entries (bulk object import start, two PlayStation™Network objects creation, and bulk object import completion) have the same group ID specified in the audit log "group" field. Operational history can be filtered by specifying a group ID in the filter options. For convenience, the UDS Management Tool also provides the **Filter table to view all associated logs** link to filter by a group ID. The link is displayed when any bulk action audit log entry rows are expanded to show details.