#### isTrivialToScan()


 bool AudioUnitPluginFormat::isTrivialToScan ( ) const overridevirtual 
 

Should return true if this format is both safe and quick to scan i.e.if a file can be scanned within a few milliseconds on a background thread, without actually needing to load an executable.Implements AudioPluginFormat.