#### saveIfNeeded()


 bool PropertiesFile::saveIfNeeded ( ) 
 

This will flush all the values to disk if they've changed since the last time they were saved.Returns false if it fails to write to the file for some reason (maybe because it's readonly or the directory doesn't exist or something).See alsosave