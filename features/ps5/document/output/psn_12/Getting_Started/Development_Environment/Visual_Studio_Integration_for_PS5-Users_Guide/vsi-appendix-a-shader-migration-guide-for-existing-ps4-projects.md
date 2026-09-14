# Visual Studio Integration for PlayStation®5 User's Guide – SDK 12.000

Source: https://game.develop.playstation.net/resources/documents/SDK/12.000/Visual_Studio_Integration_for_PS5-Users_Guide/vsi-appendix-a-shader-migration-guide-for-existing-ps4-projects.html

# Visual Studio Integration for PlayStation®5 User's Guide Appendix A - Shader Migration Guide for Existing PlayStation®4 Projects

VSI’s built-in shader support for `.pssl` files is changing with the introduction of PlayStation®5.

Previous releases of VSI provided shader support for PlayStation®4 by way of the file Item Type ‘OrbisWavePsslc’. When `.pssl` files were added to a project by creating new files or adding existing files to a project, these files were set to the ‘OrbisWavePsslc’ type. Builds always used the PlayStation®4 compiler ‘orbis-wave-psslc’.

With the addition of PlayStation®5, the default shader Item Type is now ‘WavePsslc’, for use with both PlayStation®4 and PlayStation®5. The shader compiler used during a build will be the appropriate tool for the selected platform. This will be ‘orbis-wave-psslc’ for ‘ORBIS’ or ‘prospero-wave-psslc’ for ‘Prospero’.

If you have existing projects using VSI’s shader support, OrbisWavePsslc items will continue to build as before for ‘ORBIS’ builds. For ‘Prospero’ they will be converted during the build to compile using the PlayStation®5 shader compiler.

When a new ‘Prospero’ platform configuration has been added to an existing project and configuration settings imported from ‘ORBIS’, the properties for `.pssl` files will also have been copied to the new platform configuration. Certain properties and their values are not valid or applicable on PlayStation®5. This may result in warnings during a build, and `.pssl` files not being compiled. For example, some shader profiles are not supported by prospero-wave-psslc and will result in files specifying them not being compiled during PlayStation®5 builds. Where possible, a prospero-wave-psslc profile will be substituted, but you can change this in the file property pages.

Source file header generation from a shader executable is a supported option for PlayStation®4. While the option is still available for PlayStation®5, the method is deprecated. Embedding is the preferred method when not using separate shader executables.

When selected in the **Property Pages** dialog, the Item Type for ‘OrbisWavePsslc’ will be shown as either ‘ORBIS Wave PSSL Compiler’ for PlayStation®4 configurations, or ‘Wave PSSL Compiler (deprecated)’ for PlayStation®5 configurations. For WavePsslc items, the shown Item Type will always be ‘Wave PSSL Compiler’.

Like all files, the associated item type can be switched in the **Property Pages** dialog:

While OrbisWavePsslc will automatically use prospero-wave-psslc for PlayStation®5 platform builds, it is possible to configure a project to continue using the PlayStation®4 wave compiler for these items. This is achievable by setting the property $(PlatformOrbisWavePsslc) to ‘ORBIS’ either by using a property sheet or adding the property to the project file directly:

```
<PropertyGroup>
  <PlatformOrbisWavePsslc>ORBIS</PlatformOrbisWavePsslc>
</PropertyGroup>
```