#### findPluginTypesFor()


 virtual bool KnownPluginList::CustomScanner::findPluginTypesFor ( AudioPluginFormat & format, OwnedArray< PluginDescription > & result, const String & fileOrIdentifier ) pure virtual 
 

Attempts to load the given file and find a list of plugins in it.Returnstrue if the plugin loaded, false if it crashed