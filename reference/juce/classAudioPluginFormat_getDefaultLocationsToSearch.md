#### getDefaultLocationsToSearch()


 virtual FileSearchPath AudioPluginFormat::getDefaultLocationsToSearch ( ) pure virtual 
 

Returns the typical places to look for this kind of plugin.Note that if this returns no paths, it means that the format doesn't search in files or folders, e.g. AudioUnits.Implemented in AudioUnitPluginFormat, LADSPAPluginFormat, LV2PluginFormat, VST3PluginFormat, and VSTPluginFormat.