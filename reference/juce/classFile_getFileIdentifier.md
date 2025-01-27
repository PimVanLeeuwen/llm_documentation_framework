#### getFileIdentifier()


 uint64 File::getFileIdentifier ( ) const 
 

Returns a unique identifier for the file, if one is available.Depending on the OS and filesystem, this may be a unix inode number or a win32 file identifier, or 0 if it fails to find one. The number will be unique on the filesystem, but not globally.