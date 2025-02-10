#### fileMightContainThisPluginType()


 bool VSTPluginFormat::fileMightContainThisPluginType ( const String & fileOrIdentifier ) overridevirtual 
 

Should do a quick check to see if this file or directory might be a plugin of this format.This is for searching for potential files, so it shouldn't actually try to load the plugin or do anything timeconsuming.Implements AudioPluginFormat.