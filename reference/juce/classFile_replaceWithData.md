#### replaceWithData()


 bool File::replaceWithData ( const void \* dataToWrite, 
 
 size\_t numberOfBytes ) const 

Replaces this file's contents with a given block of data.This will delete the file and replace it with the given data.A nice feature of this method is that it's safe instead of deleting the file first and then rewriting it, it creates a new temporary file, writes the data to that, and then moves the new file to replace the existing file. This means that if the power gets pulled out or something crashes, you're a lot less likely to end up with a corrupted or unfinished file..Returns true if the operation succeeds, or false if it fails.See alsoappendText Referenced by StandalonePluginHolder::askUserToSaveState().