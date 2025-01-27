#### moveFileTo()


 bool File::moveFileTo ( const File & targetLocation ) const 
 

Moves or renames a file.Tries to move a file to a different location. If the target file already exists, this will attempt to delete it first, and will fail if this can't be done.Note that the destination file isn't the directory to put it in, it's the actual filename that you want the new file to have.Also note that on some OSes (e.g. Windows), moving files between different volumes may not be possible.This function will often fail to move directories because of the ambiguities about merging existing directories. Use copyDirectoryTo() and deleteRecursively() in these situations.Returnstrue if the operation succeeds