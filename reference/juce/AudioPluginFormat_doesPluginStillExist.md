#### doesPluginStillExist()


 virtual bool AudioPluginFormat::doesPluginStillExist ( const PluginDescription & ) pure virtual 
 

Checks whether this plugin could possibly be loaded.It doesn't actually need to load it, just to check whether the file or component still exists.Implemented in AudioUnitPluginFormat, LADSPAPluginFormat, LV2PluginFormat, VST3PluginFormat, and VSTPluginFormat.