#### addFile()


 void ZipFile::Builder::addFile ( const File & fileToAdd, 
 
 int compressionLevel, 
 const String & storedPathName = String() ) 

Adds a file to the list of items which will be added to the archive.The file isn't read immediately: the files will be read later when the writeToStream() method is called.The compressionLevel can be between 0 (no compression), and 9 (maximum compression). If the storedPathName parameter is specified, you can customise the partial pathname that will be stored for this file.