#### findAllTypesForFile()


 void VSTPluginFormat::findAllTypesForFile ( OwnedArray< PluginDescription > & results, const String & fileOrIdentifier ) overridevirtual 
 

This tries to create descriptions for all the plugin types available in a binary module file.The file will be some kind of DLL or bundle.Normally there will only be one type returned, but some plugins (e.g. VST shells) can use a single DLL to create a set of different plugin subtypes, so in that case, each subtype is returned as a separate object.Implements AudioPluginFormat.