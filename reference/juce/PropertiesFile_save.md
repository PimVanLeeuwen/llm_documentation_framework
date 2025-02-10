#### save()


 bool PropertiesFile::save ( ) 
 

This will force a writetodisk of the current values, regardless of whether anything has changed since the last save.Returns false if it fails to write to the file for some reason (maybe because it's readonly or the directory doesn't exist or something).See alsosaveIfNeeded