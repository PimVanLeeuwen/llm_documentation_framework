#### copyFileTo()


 bool File::copyFileTo ( const File & targetLocation ) const 
 

Copies a file.Tries to copy a file to a different location. If the target file already exists, this will attempt to delete it first, and will fail if this can't be done.Note that the target file isn't the directory to put it in, it's the actual filename that you want the new file to have.Returnstrue if the operation succeeds