#### searchPathsForPlugins()


 StringArray LADSPAPluginFormat::searchPathsForPlugins ( const FileSearchPath & directoriesToSearch, bool recursive, bool allowPluginsWhichRequireAsynchronousInstantiation ) overridevirtual 
 

Searches a suggested set of directories for any plugins in this format.The path might be ignored, e.g. by AUs, which are found by the OS rather than manually.Parameters

 directoriesToSearch This specifies which directories shall be searched for plugins. 
 
 recursive Should the search recursively traverse folders. 
 allowPluginsWhichRequireAsynchronousInstantiation If this is false then plugins which require asynchronous creation will be excluded. 


Implements AudioPluginFormat.