# Param.json File Specification – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Param_Json-Specification/overriding-the-param-file-of-the-application-package-applica.html

# Using the Param File (param.json)

This topic describes how to create, verify and use param files
(param.json).

## Creating the Param File

Param files are JSON format files, and it is possible to create them using a generic text editor without using Param Editor.

Refer to the [Param Editor User's Guide](../Param_Editor-Users_Guide/__document_toc.html) document for information about how to create a
param file using Param Editor.

Refer to the [Param File (param.json) Specifications](param-file-paramjson-specifications.html "Param files are written in the JSON format. If you are creating the param file using a generic text editor, make sure the param file conforms to the JSON format: in particular, make sure that the param file does not contain the byte order mark (BOM) character and that the character encoding is UTF-8.") chapter for information about how to create a param file without using Param Editor.

## Verifying the Param File

Verify the created param file using Param Editor or Publishing Tools Command Line Version to make sure that there aren't any missed configuration items or format violations.

Refer to the [Param Editor User's Guide](../Param_Editor-Users_Guide/__document_toc.html) document or the [Publishing Tools Command Line
Version User's Guide](../Publishing_Tools_CL-Users_Guide/__document_toc.html) document for information about how to verify the param file.

## Using the Param File

Use the created param file by placing it in the designated directory within the application
file set. Refer to the [Application Content Overview](../Application_Content-Overview/__document_toc.html) document for details.

# Overriding the Param File of the Application Package (Application Development Support)

The host tools can start an application by specifying a param.json file that overrides
some of the param.json parameters from the package. This feature is available in DevKit
Development mode, DevKit Assist mode, and TestKit Assist mode.

```
%prospero-run.exe /overrideParam:<param.json file path on the host> /app <titleId>
```

Refer to the [Target Manager CLI User's Guide](../Target_Manager_CLI-Users_Guide/__document_toc.html) for more details about prospero-run.exe.

Note: Only the following parameters can be overridden. Trying to override other parameters
will cause an error.

* kernel/flexibleMemorySize
* kernel/cpuPageTableSize
* kernel/gpuPageTableSize
* amm/pagetableMemorySizeInMib
* amm/vaRangeInGib
* amm/multimapVaRangeInGib
* psml/mfsrVersion

Note: To use this feature, the param.json file must be extracted from the package. You can do
this by using the following
command:

```
%prospero-pub-cmd.exe img_extract --no_passcode <package file name>:/sce_sys/param.json param.json
```

Refer
to the [Publishing Tools Command Line Version User's Guide](../Publishing_Tools_CL-Users_Guide/__document_toc.html) for details about
prospero-pub-cmd.exe.