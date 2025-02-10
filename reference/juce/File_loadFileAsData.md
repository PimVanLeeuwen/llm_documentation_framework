#### loadFileAsData()


 bool File::loadFileAsData ( MemoryBlock & result ) const 
 

Loads a file's contents into memory as a block of binary data.Of course, trying to load a very large file into memory will blow up, so it's better to check first.Parameters

 result the data block to which the file's contents should be appended note that if the memory block might already contain some data, you might want to clear it first 
 



Returnstrue if the file could all be read into memory Referenced by StandalonePluginHolder::askUserToLoadState().