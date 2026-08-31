# Advanced Player Profile Editor User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Advanced_Player_Profile_Editor-Users_Guide/saving-and-deleting.html

# Editing Advanced Player Profile Properties

# Editing Properties

This topic provides information on how to select the properties you want to edit.

After you have selected the account for PlayStation™Network whose properties you want to modify and have also selected the context (**NPCommID**) for the account, you can select which properties you would like to mock-up/test.

Each Property group displays in a drop-down list with the name of the property group and
the name of the attribute listed on the top unexpanded level of the drop-down list. Each
list has a "+". Clicking the "+" opens the property for editing (see the figure below).

Figure 2. Property Groups

# Property States and API States

This topic provides information on property and API states.

There are indicators in each property group to display the current state of the property.
These states reflect whether the property is currently being edited or whether any changes
you made have been saved to the back end (see the figure below). The various States are as
follows:

* No API Overrides Applied - The property has no fake data/overrides on the back end.
* Overrides applied - The property has fake data or overrides on the back end.
* No Edits - No changes have been made to the form.
* Editing - Changes have been entered in the forms but not saved.
* Edits Saved - Changes have been made in the form and saved to the back end.

Figure 3. Property States and API States

# Saving and Deleting

This topic provides information on saving and deleting edits you've made to
properties.

After you have made your selected changes to various property values you can then either save or delete them. Saving your selected edits saves them to the back end and enables you to test. Deleting removes your changes from the back end and removes fake data from the account.

To save changes for a given property group click the Save button located inside the
property list. To save changes to the entire list of properties for a given account, click
the Save All located at the top of the page in the upper right-hand corner. The save
buttons are not selectable if there are no new edits to apply (See the figure below).

Figure 4. Saving

To delete changes for a given property click the trash can icon located next to the
Overrides Applied indicator in the top line of the given property group. Note that the
trash can icon is not present if there are no changes to be deleted. There is no global
delete option for all given properties for an account (see the figure below).

Figure 5. Deleting

# Confidence Values

The Advanced Player Profile editor allows you to see different confidence values for each property you choose to add fake data to.

The values you can select for confidence are:

* 0
* 25
* 50
* 75
* 100

These values are in percentages, with 100 being complete confidence and 0 being no confidence.