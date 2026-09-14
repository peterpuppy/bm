# Workspaces Overview – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Workspaces-Overview/workspaces-overview-appendix-c-reparse-points-and-hard-links-support.html

# Workspaces Overview Appendix C - Reparse Points and Hard Links Support

Workspace file systems do not have an equivalent concept to Host PC filesystem **reparse
points** such as
symbolic
links
(symlinks),
directory junction
points,
volume mount
points
and hard
links.

Adding Host PC filesystem reparse points to Workspaces is supported but with some
[limitations](workspaces-overview-appendix-c-reparse-points-and-hard-links-support.html#workspaces-overview_9__section_m3b_p4m_zgc),
which are detailed in
later
in this topic.

When a reparse point or hard link is transferred to a workspace, the underlying file or
directory is instead duplicated to a separate entry in the filesystem. This applies for
both [Standalone](workspaces-overview-appendix-c-reparse-points-and-hard-links-support.html#workspaces-overview_9__section_yzj_n4m_zgc)
and [System Managed Host
Mirror](workspaces-overview-appendix-c-reparse-points-and-hard-links-support.html#workspaces-overview_9__section_e2x_n4m_zgc)
workspaces.

It is recommended that [GP5 Files](using-gp5-files-in-workspaces.html) are
used as an alternative to reparse points and hard links to avoid the following
limitations.

## Standalone

File contents from reparse points and hard links can be pushed to a
Standalone
workspace. The reparse entries being pushed will be resolved by the CLI and GUI
tools, and the contents of their sources will be pushed as expected.

The path of the filesystem entry created in the workspace for the reparse point or
hard link will reflect the path of the reparse point or hard link on the Host PC
filesystem.

## System Managed Host Mirror

The use of a Host PC working directory or GP5 mapped paths containing reparse points
or hard links is supported. Files referenced by reparse points and hard links will
automatically be mirrored to the System Managed Host Mirror workspace when requested
by a running process.

[Host File
System Monitoring](host-file-system-monitoring.html) can also detect content changes made from either the
reparse points entries or from their sources, but there are some limitations
regarding their use.

## Limitations

* Changing reparse point entries while file monitoring is active may lead to
  synchronization issues. This is because file monitoring may not be able to
  detect file changes from these reparse entries. For example, if a reparse
  entry from a mirrored directory is renamed while file monitoring is active,
  subsequent files changes under the renamed reparse entry may not be
  detected.
* The use of hard links is allowed for both Standalone and System Managed Host
  Mirror workspaces, but the links will be treated as different files. File
  changes to a link will not affect other links which can lead to
  synchronization issues for the System Managed Host Mirror workspace.
* Although reparse points and hard links can be pushed from the Host PC
  filesystem into a Standalone workspace, pulling the contents back to the
  Host PC will not recreate the same reparse points and hard links entries as
  the workspace does not retain any information related to the original
  reparse points and hard links.
* It is possible to have a symlink directory pointing to a location in a way
  that creates a circular reference. Both CLI and GUI tools are not able to
  handle circular references and their use should be avoided.
* The combined use of different reparse points mechanisms (for example, a
  symbolic link directory containing a mounted folder inside of it and vice
  versa) can lead to synchronization issues.
* Broken reparse points will lead to system errors when using CLI and GUI
  tools. For example, pushing a folder containing a broken symlink file will
  make the operation to fail due an `ERROR_FILE_NOT_FOUND`
  Windows system error.