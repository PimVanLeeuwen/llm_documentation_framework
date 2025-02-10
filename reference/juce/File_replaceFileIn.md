#### replaceFileIn()


 bool File::replaceFileIn ( const File & targetLocation ) const 
 

Replaces a file.Replace the file in the given location, assuming the replaced files identity. Depending on the file system this will preserve file attributes such as creation date, short file name, etc.If replacement succeeds the original file is deleted.Returnstrue if the operation succeeds