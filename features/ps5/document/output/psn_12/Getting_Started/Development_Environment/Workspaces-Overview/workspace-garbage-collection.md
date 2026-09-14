# Workspaces Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Workspaces-Overview/workspace-garbage-collection.html

# Workspace Garbage Collection

When you repeatedly modify a workspace, for example by repeatedly hot loading files, extra unnecessary data will accumulate. We call this garbage data and if the garbage data is allowed to build up there is a risk that you will not be able to add or update files on that workspace.

To avoid this issue you can enable **Workspace Garbage Collection** to check the garbage data in the workspace whenever the following operations are completed:

* `prospero-ctrl workspace push`
* `prospero-ctrl workspace deploy`
* `prospero-ctrl workspace mirror-push`
* `prospero-ctrl workspace mirror-deploy`
* File transfer from the Host PC to the Target using Workspace Explorer.
* Bulk copy from USB drive to workspace.

If, once one of the above operations is completed, the system decides the garbage data levels are too high, **Workspace Garbage Collection** is automatically triggered and the garbage data is removed from the workspace.

To turn on Workspace Garbage collection:

1. Open the Target Settings application.
2. In Target Settings, under the ★**Debug Settings > System** heading, set **Enable Workspace Garbage Collection** to On.

OR

* Using the system software on the Target, navigate to ★**Debug Settings > System** and set **Enable**
  **Workspace Garbage Collection** to On.

Note:

Setting **Enable Workspace Garbage Collection** to On will apply it to all existing or new workspaces immediately.

## Limitations

**Workspace Garbage Collection** has the following limitations:

* Even with **Workspace Garbage Collection** enabled, you may not be able to add or update files even though you have enough free space. In this case it is necessary to manually delete any files that are no longer required from the workspace, or recreate the workspace.
* Depending on the number and size of files in your workspace, the completion of the operations that trigger workspace garbage collection may be delayed for a short time. This may cause delays in the utilizing the workspace.
* Even after **Workspace Garbage Collection** is complete, the size of the garbage data retrieved by `prospero-ctrl workspace list` or `prospero-ctrl workspace list` /`full` may not change.