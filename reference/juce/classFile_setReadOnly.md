#### setReadOnly()


 bool File::setReadOnly ( bool shouldBeReadOnly, 
 
 bool applyRecursively = false ) const 

Changes the writepermission of a file or directory.Parameters

 shouldBeReadOnly whether to add or remove writepermission 
 
 applyRecursively if the file is a directory and this is true, it will recurse through all the subfolders changing the permissions of all files 



Returnstrue if it manages to change the file's permissions. 
See alsohasWriteAccess