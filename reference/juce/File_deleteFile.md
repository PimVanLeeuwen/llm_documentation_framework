#### deleteFile()


 bool File::deleteFile ( ) const 
 

Deletes a file.If this file is actually a directory, it may not be deleted correctly if it contains files. See deleteRecursively() as a better way of deleting directories.If this file is a symlink, then the symlink will be deleted and not the target of the symlink.Returnstrue if the file has been successfully deleted (or if it didn't exist to begin with). 
See alsodeleteRecursively