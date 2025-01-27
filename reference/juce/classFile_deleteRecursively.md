#### deleteRecursively()


 bool File::deleteRecursively ( bool followSymlinks = false ) const 
 

Deletes a file or directory and all its subdirectories.If this file is a directory, this will try to delete it and all its subfolders. If it's just a file, it will just try to delete the file.Parameters

 followSymlinks If true, then any symlink pointing to a directory will also recursively delete the contents of that directory 
 



Returnstrue if the file and all its subfolders have been successfully deleted (or if it didn't exist to begin with). 
See alsodeleteFile