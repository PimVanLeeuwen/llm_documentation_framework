#### searchPathsForPlugins()


 virtual StringArray AudioPluginFormat::searchPathsForPlugins ( const FileSearchPath & directoriesToSearch, bool recursive, bool allowPluginsWhichRequireAsynchronousInstantiation = false ) pure virtual 
 

Searches a suggested set of directories for any plugins in this format.The path might be ignored, e.g. by AUs, which are found by the OS rather than manually.Parameters

 directoriesToSearch This specifies which directories shall be searched for plugins. 
 
 recursive Should the search recursively traverse folders. 
 allowPluginsWhichRequireAsynchronousInstantiation If this is false then plugins which require asynchronous creation will be excluded. 


Implemented in AudioUnitPluginFormat, LADSPAPluginFormat, LV2PluginFormat, VST3PluginFormat, and VSTPluginFormat.