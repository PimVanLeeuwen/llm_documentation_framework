#### isTrivialToScan()


 virtual bool AudioPluginFormat::isTrivialToScan ( ) const pure virtual 
 

Should return true if this format is both safe and quick to scan i.e.if a file can be scanned within a few milliseconds on a background thread, without actually needing to load an executable.Implemented in AudioUnitPluginFormat, LADSPAPluginFormat, LV2PluginFormat, VST3PluginFormat, and VSTPluginFormat.