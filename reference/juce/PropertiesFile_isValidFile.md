#### isValidFile()


 bool PropertiesFile::isValidFile ( ) const noexcept 
 

Returns true if this file was created from a valid (or nonexistent) file.If the file failed to load correctly because it was corrupt or had insufficient access, this will be false.