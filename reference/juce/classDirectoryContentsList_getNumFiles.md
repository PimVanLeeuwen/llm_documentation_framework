#### getNumFiles()


 int DirectoryContentsList::getNumFiles ( ) const noexcept 
 

Returns the number of files currently available in the list.The info about one of these files can be retrieved with getFileInfo() or getFile().Obviously as the background thread runs and scans the directory for files, this number will change.See alsogetFileInfo, getFile