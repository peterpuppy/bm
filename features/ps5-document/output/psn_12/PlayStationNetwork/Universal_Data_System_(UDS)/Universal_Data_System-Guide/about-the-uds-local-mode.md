# Universal Data System Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Universal_Data_System-Guide/about-the-uds-local-mode.html

# Local Development Workflow

The Local
Development Workflow is a server independent workflow that facilitates rapid, local
development cycles for testing UDS implementation in applications.

This workflow enables you to define, update, and test UDS entities, such as
PlayStation™Network objects, UDS events, UDS stats, and trophies, prior to uploading
data to the server.

This chapter describes how to build a development environment, how to develop in the
Local Development Workflow, and how to use the
`np-universal-data-system-local-tool` during development.

# Supported Features

This topic lists the features that the Local Development Workflow supports.

The Local Development Workflow supports the following features:

## Activities

Only single-player activities in the `progress` and
`openEnded` categories can be handled in the Local Development
Workflow. You can define these activities using
`np-universal-data-system-local-tool`. Activities from other
categories and Game Help are not supported.

Use **Activity Debugging** to check activities on DevKit/TestKit in Local Mode. Other screens such as Game Hub and Control Center do not support showing activities in Local Mode. For more information about Activity Debugging, see [Game Intent System Overview - Debugging Support for Developing Game Intent-Compatible Applications](../Game_Intent_System-Overview/debugging-support-using-the-system-software.html).

## Trophies

You can check trophy definitions and progress on the UI of the system software when DevKit/TestKit is set to Local Mode. For more information, see [Trophy System Overview - Debugging Support Provided by the System Software](../Trophy_System-Overview/debugging-support-provided-by-the-system-software.html).

# UDS Local Mode

Local mode is
a unique mode for DevKit and TestKit that's required for development in the Local
Development Workflow. Local Mode is only available when *Release Check Mode* is set
to *Development Mode* or *Assist Mode*.

The normal mode is called Server Mode.

In Local Mode, the system refers to the local UDS and trophy configuration created by
`np-universal-data-system-local-tool`, rather than the UDS and trophy
configuration created by the UDS Management Tool that you can download from GEMS as
`npconfig.zip`.

In Local Mode, UDS events posted by games using the NpUniversalDataSystem SDK are not
sent to the server. Also, UDS stats and state configurations updated using the
NpUniversalDataSystem SDK are not synchronized with the server.

## UDS Data Saved in Local Mode

UDS events, stats, and state data posted from games in Local Mode is managed
separately from Server Mode data. This means you cannot access data stored in Local
Mode if you switch the development mode to Server Mode. Ensure your development mode
is set to **Local Mode** to access UDS data posted during local development.

Local Mode only stores data for one title at a time. If you start local development
for a different title, or a version of the same title with different UDS and trophy
configurations, the system deletes saved data in Local Mode. This means you can
update your UDS and trophy configurations without worrying about compatibility
between updates.

If you want to explicitly delete data posted in Local Mode:

* For UDS data, go to **★Debug Settings** > **PlayStation™Network** >
  **Universal Data System Development data** > **Delete data of all
  users (console)**.
* For trophies, from the Trophies System UI, go to **Options** > **★Delete
  All Users' Trophies (Console)**

You can also use the `prospero-ctrl` command:

```
> prospero-ctrl application delete-data uds console
> prospero-ctrl application delete-data trophy console
```

Deleting data from Local Mode does not affect data stored in other development
modes.

# Developing in the Local Development Workflow

This topic provides an overview of the procedure for developing in the Local Development Workflow. The Local Development Workflow allows development to proceed independently of the server.

Using only the host machine and DevKit or TestKit, you can update UDS object and trophy
configurations and check results in a short cycle without affecting other
developers.

When developing using the Local Development Workflow, you'll generally follow these
steps:

1. Register your product and request necessary services.
2. Set up DevKit/TestKit.
3. Configure UDS entities.
4. Implement UDS event posting.
5. Run your application.
6. Check the results. If the results are not what you expect, repeat steps 3-6
   until you get the results you expect from your implementation.

## Registering Products and Requesting Services

As with normal development workflows, product registration and service requests are
required when using the Local Development Workflow. If you haven't already done so,
follow the [PlayStation™Network Service Setup Guide](../PSN_Service_Setup-Guide/__document_toc.html) to create a product and obtain
an `nptitle.dat` file. To create a `param.json` file,
see [Param.json File Specification](../Param_Json-Specification/__document_toc.html).

You do not need to prepare a dedicated product for development with the Local
Development Workflow. If your application is ready to use UDS, you can use
`nptitle.dat` and `param.json` as they are.

## Setting up DevKit/TestKit

After you've registered your product and requested the necessary services, you can
set up DevKit/TestKit.

To set up DevKit/TestKit:

1. Confirm that the **Release Check** mode of DevKit/TestKit is set to
   **Development Mode** or **Assist Mode**.
2. Go to **★Debug Settings** > **PlayStation™Network**.
3. Set **Universal Data System Development Mode** to **Local Mode**.
4. Set **Universal Data System Debug Log** to **ON**.

You can also update these settings using the *Target Settings* application from
the host machine.

## Configuring UDS Entities

After you've set up DevKit/TestKit, you can configure the UDS entities you'll use during local development.

Create or update json and image files that define your UDS entities and run
`np-universal-data-system-local-tool` using the files you create
as inputs. `np-universal-data-system-local-tool` converts the input
files to a format that the DevKit/TestKit system software can interpret. The tool
then places the files in the application's `sce_sys` directory.

For information on how to use `np-universal-data-system-local-tool`,
see [Using the
NPUniversalDataSystem Local Tool](np-universal-data-system-local-tool.html "This topic covers the procedure for using the NpUniversalDataSystem tool when developing in the Local Development Workflow.").

## Implementing UDS Event Posting

There is no need for a dedicated implementation on the application side to operate in
Local Mode. You can post defined UDS events as you normally would. Behavior of the
NpUniversalDataSystem library used for UDS event posting does not differ between
Local Mode and Server Mode.

## Running the Application

After you've posted your UDS events, run the application to check that your
implementation is working as expected.

Run your application from a development environment such as Visual Studio, or
transfer to a Workspace before starting. After you start the application, post your
UDS event data.

When you run your application, DevKit/TestKit reads UDS object and trophy
configuration data generated by
`np-universal-data-system-local-tool`. The system software displays
the latest configuration of UDS object and trophy data.

If the configuration data has been updated since the last run, existing UDS stats,
state, and trophy acquisition information is cleared and rebuilt from UDS events
posted in subsequent gameplay.

Additionally, you can package your application, install it in DevKit/TestKit, and run
it. To create a game package for Local Mode, include the following files created by
`np-universal-data-system-local-tool` in the package:

* `sce_sys/uds_local.json`
* `sce_sys/uds/npbind_local.json`
* `sce_sys/uds/uds00_local.ucp`
* `sce_sys/trophy2/npbind_local.json`
* `sce_sys/trophy2/trophy00_local.ucp`

Game packages containing these files are only available for development. You
cannot submit packages that contain these files.

## Checking the Results

Since data is not sent to the server in Local Mode, you can't check UDS event, stats,
and state data in the UDS Management Tool. Instead, you must use the UDS Debug Log.
Enabling the UDS Debug Log allows you to check posted UDS events and updated stats
and state data on the console output.

For details on using the UDS Debug Log, see [NpUniversalDataSystem Library Overview -
Using the Library - Debug Support Through the System Software](../NpUniversalDataSystem-Overview/debug-support-through-the-system-software.html).

Check activity and trophy information from the UI of the system software. See [Supported Features](np-universal-data-system-local-tool.html "This topic covers the procedure for using the NpUniversalDataSystem tool when developing in the Local Development Workflow.") for
more information.

# Using the NpUniversalDataSystem Local Tool

This topic covers the procedure for using the NpUniversalDataSystem tool when
developing in the Local Development Workflow.

When developing in Local Mode as part of the Local Development Workflow, UDS event,
stats, and state data is managed separately from data in Server Mode. The system refers
to the local UDS object and trophy configuration created by
`np-universal-data-system-local-tool`, rather than the UDS object and
trophy configuration created by the UDS Management Tool. This means you must format UDS
entities using `np-universal-data-system-local-tool` for DevKit/TestKit
to properly interpret UDS data.

For more information on the Local Development Workflow and Local Mode, see [UDS Local Mode](about-the-uds-local-mode.html "Local mode is a unique mode for DevKit and TestKit that's required for development in the Local Development Workflow. Local Mode is only available when Release Check Mode is set to Development Mode or Assist Mode.").

Once UDS entities are verified through local testing, you can use
`np-universal-data-system-local-tool` to upload data to the
development environment of the UDS server. You can access uploaded data in the Universal
Data System Management Tool.

## Overview

`np-universal-data-system-local-tool` is a command line tool that is
installed on the host machine. To use the tool:

1. Create an input folder that contains the UDS entities and associated image files
   you want to format.
2. Prepare the output folder (`sce_sys`) to receive generated
   content.
3. Run the tool in your terminal.

## Creating the Input Folder

Create an input folder that contains all input files to be formatted, as well as all
referenced images. Place images in a `/images` subfolder. Specify
image URLs in the input files as `images/XXXX.png`.

Example Input Folder

Input files for a particular entity type should not be present if no entity of the
type is specified, for example, do not include
`events_defintion.json` if you haven't defined any UDS events.

## Preparing the Output Folder

To prepare the output folder:

1. Specify your game’s `sce_sys` folder as the target output folder.
   The output folder must contain `param.json` and
   `nptitle.dat` files. See [Param.json File Specification -
   Using the Param File (param.json)](../Param_Json-Specification/using-the-param-file-paramjson.html) for information on creating the
   `param.json` file.
2. Obtain the `nptitle.dat` file from `NPConfig.zip`.
   See [Package/Disc Management Tool (GEMS) Overview](../Package_Disc_Management_Tool_GEMS-Overview/__document_toc.html) for more information.

## Running `np-universal-data-system-local-tool`

`np-universal-data-system-local-tool` has parameters that you can add
to define how your UDS entities are formatted and uploaded to the UDS server.

```
np-universal-data-system-local-tool.exe [command name] -options -input
```

* **Command Name** - Optional command that instructs
  `np-universal-data-system-local-tool` to format local testing
  data or submit it to the UDS server. Available commands include:
  + `generate` - Formats the data for testing in Local Mode.
    This is the default setting when running the tool.
  + `sync` - Submits the data to the UDS server.
* **Options** - Options that you can choose to define the data being formatted,
  such as default language, the Np service label to be used in generated output,
  and the path to the target output directory. You can use "/" or "-" to indicate
  the use of an option. For example, `/defaultLanguage` or
  `-defaultLanguage`.
* **Input** - Input files of the UDS entities to be formatted. Each entity is
  defined in a separate file, for example, `events_definition.json`
  and `stats_definition.json`. Input files must be in json
  format.

See [Valid Options and Input
Files](np-universal-data-system-local-tool.html#topic_ttj_xx3_5xb__table_vnz_pcp_xxb) for a full list of available options and input files.

## Using the Generate Command

The `generate` command formats UDS data for testing in Local Mode.
This is the default setting when running the tool. To format your UDS entities, run
the tool using your input and output files as parameters:

```
np-universal-data-system-local-tool.exe -o [your output file location] <your input file location>
```

The tool provides a **Return Code** which details information on the success of
the tool. The command line tool returns 0 if the program was successfully executed,
and 1 if the program encounters any errors.

If the input files have validation errors or the output generation process fails, the
tool displays an error message on the console and generates a log file.
Additionally, the processing ends in an error. Every execution of the tool generates
a new log file. Log files are saved in your specified output folder.

**Testing the Output**

Use the Target Manager and Workspace Explorer services to push the output file to
your DevKit for testing. For more information on these services, see [Target
Management Applications UI Overview](../TM_Applications_UI-Overview/__document_toc.html) and [Workspace Explorer User's Guide](../Workspace_Explorer-Users_Guide/__document_toc.html).

## Using the Sync Command

The `sync` command submits UDS data to the UDS server using the
Universal Data System Configuration Web API. For more information, see [Universal
Data System Configuration Web API Reference](../../../WebAPI/latest/Universal_Data_System_Configuration_WebAPI-Reference/__document_toc.html).

**Obtaining Client Credentials**

The PlayStation™Network Web API requires a client-credential access token for
authorization. You must provide client ID and client secret credentials to the
`np-universal-data-system-local-tool` when using the
`sync` command.

Client ID and client secret credentials are available when creating a Back Office
Server product. For information on how to create new products, see
[PlayStation™Network Service Setup Guide - Registering Titles - Creating a New
Product](../PSN_Service_Setup-Guide/creating-a-new-product.html).

Note: Handle client ID and client secret credentials securely.
SIE recommends that you only use the sync command on a server where client ID
and client secret credentials are stored securely. Do not use the sync command
from a location where client ID and client secret credentials can be exposed to
unauthorized users, for example, a developer's desktop.

**Running the Sync Command**

Once the input folder and client credentials are ready, run the following to initiate
the upload:

```
np-universal-data-system-local-tool.exe sync /client_id <client id value> /client_secret_path <path to your client secret file> <your input file location>
```

If the input files have validation errors or the output generation process fails, the
tool displays an error message on the console and generates a log file.
Additionally, the processing ends in an error. Every execution of the tool generates
a new log file. Log files are saved in your specified output folder.

Review and update uploaded data using the Universal Data System Management Tool. See
[Universal Data System Guide - Using the UDS Management Tool - Accessing the Tool](accessing-the-tool.html)
for more information.

## Valid Options and Input Files

The following tables describe valid options and input files you can use:

np-universal-data-system-local-tool.exe Options

| Option | Description | Applicable Command |
| --- | --- | --- |
| `/npServiceLabel`, `/np_service_label`, or `/sl` | When used with the **generate** command, the value you provide is used in the output file `npbind_local.json`. Any value you specify has no effect in the local development workflow. When used with the **sync** command, the value you provide is used as a target Np service label for uploading UDS entities. Obtain the Np service label from your Back Office Server product. The default value is 0. | **generate** and **sync** |
| `/defaultLanguage`, `/default_language`, or `/dl` | Default language for the game. Default value is `en-US`. For valid language codes, see [Auth Web API Overview - Appendix - Language Codes](../../../WebAPI/latest/Auth_WebAPI-Overview/language-codes.html). | **generate** and **sync** |
| `/output` or `/o` | Path to the target folder for generated output. The default path is the folder where `np-universal-data-system-local-tool.exe` is running. | **generate** and **sync** |
| `/verbose` or `/v` | Generate verbose information to the console output. The default value is `false`. | **generate** and **sync** |
| `/overwrite` or `/ow` | Boolean value (true or false) to determine if all existing entities that can be deleted should be deleted prior to the upload. The default value is `false`. | **sync** |
| `/client_id` or `/cid` | Client ID assigned in the Back Office Server product created in DevNet. Required when using the `sync` command. | **sync** |
| `/client_secret_path` or `/csp` | Path to the client secret location. Obtain the client secret on DevNet from your Back Office Server product. Required when using the `sync` command. | **sync** |
| `/help` or `/h` | Display help information for using the tool. | **generate** and **sync** |

np-universal-data-system-local-tool.exe Input Files

| File Name | Description |
| --- | --- |
| `objects_definition.json` | Includes definitions of all PlayStation™Network objects. `np-universal-data-system-local-tool` supports activities, tasks, subtasks, and subcategories. `np-universal-data-system-local-tool` When using **generate** command, only supports activities in the `progress` or `openEnded` categories, with `isOnlineMultiplay` set to false. When using **sync**command, all activities are supported. All other PlayStation™Network objects are ignored by both **generate** and **sync** commands |
| `events_definition.json` | Includes definitions of UDS events. |
| `stats_definition.json` | Includes definitions of UDS stats. |
| `stats_extraction.json` | Includes definitions of UDS stats extractions. |
| `Trophies_definition.json` | Includes definitions of trophy set, trophy groups, and trophies. |

Input files must conform to the schema of the UDS Configuration Web API. For details,
see [Universal Data System Configuration Web API Reference](../../../WebAPI/latest/Universal_Data_System_Configuration_WebAPI-Reference/__document_toc.html).