#### moveToTrash()


 bool File::moveToTrash ( ) const 
 

Moves this file or folder to the trash.Returnstrue if the operation succeeded. It could fail if the trash is full, or if the file is writeprotected, so you should check the return value and act appropriately.