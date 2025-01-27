#### setDirectory()


 void DirectoryContentsList::setDirectory ( const File & directory, 
 
 bool includeDirectories, 
 bool includeFiles ) 

Sets the directory to look in for files.If the directory that's passed in is different to the current one, this will also start the background thread scanning it for files.