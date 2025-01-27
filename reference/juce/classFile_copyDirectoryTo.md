#### copyDirectoryTo()


 bool File::copyDirectoryTo ( const File & newDirectory ) const 
 

Copies a directory.Tries to copy an entire directory, recursively.If this file isn't a directory or if any target files can't be created, this will return false.Parameters

 newDirectory the directory that this one should be copied to. Note that this is the name of the actual directory to create, not the directory into which the new one should be placed, so there must be enough write privileges to create it if it doesn't exist. Any files inside it will be overwritten by similarly named ones that are copied.