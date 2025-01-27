#### hasWriteAccess()


 bool File::hasWriteAccess ( ) const 
 

Checks whether a file can be created or written to.Returnstrue if it's possible to create and write to this file. If the file doesn't already exist, this will check its parent directory to see if writing is allowed. 
See alsosetReadOnly