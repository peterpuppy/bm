# Visual Studio Integration for PlayStation®5 User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Visual_Studio_Integration_for_PS5-Users_Guide/vsi-appendix-b-user-hosted-msbuild-platform-files.html

# Visual Studio Integration for PlayStation®5 User's Guide Appendix B - User Hosted MSBuild Platform Files

When VSI is installed, a collection of files is also copied into MSBuild to extend its C++ support to include the PlayStation®5 platform. These files are housed under MSBuild’s Platforms folder in a directory called Prospero.

In Visual Studio 2026, the Platforms folder can be found under:

```
C:\Program Files\Microsoft Visual Studio\18\<Edition>\MSBuild\Microsoft\VC\v180
```

In Visual Studio 2022, the Platforms folder can be found under:

```
C:\Program Files\Microsoft Visual Studio\2022\<Edition>\MSBuild\Microsoft\VC\v170
```

In Visual Studio 2019, the Platforms folder can be found under:

```
C:\Program Files (x86)\Microsoft Visual Studio\2019\<Edition>\MSBuild\Microsoft\VC\v160
```

These files are used automatically by MSBuild when Visual Studio loads a project that contains configurations for PlayStation®5.

It is possible to copy the files from MSBuild’s `Prospero` directory to another location and have MSBuild use these files when building projects rather than those installed by VSI. This is a useful feature as it enables teams working on shared source to also share the same platform files used to build them regardless of the version of VSI installed by users. These files can be stored alongside the game source and SDK files and placed under source control.

Setting the project property `$(ProsperoPlatformFolder)` will cause MSBuild to assume the `Prospero` folder is at the location specified. This property can be set directly in the project files that want to specify their own MSBuild platform files. Or alternatively, a useful feature of MSBuild can be used to specify the folder’s use across all project files in the game. If a file called `Directory.Build.props` is placed alongside or in a directory above a project, its contents are incorporated into it.

For example, if the `Prospero` folder has been placed at the location `C:\MyGame\Platforms\Prospero`, then creating a file `Directory.Build.props` in `C:\MyGame` with the following contents will redirect MSBuild to the new `Prospero` location for any projects that exist under MyGame:

```
<Project>
  <PropertyGroup>
    <ProsperoPlatformFolder>$(MSBuildThisFileDirectory)\MSBuild\Prospero\
    </ProsperoPlatformFolder>
  </PropertyGroup>
</Project>
```

Alternatively, the property can be set as a System Environment variable on the PC. For example:

```
>set ProsperoPlatformFolder=C:\MyGame\Platforms\Prospero\
```

Note:

The one limitation for this feature to work is that the user needs to have **VSI for PlayStation®5** v3.00.0.x or later installed to enable redirection to the user hosted files.