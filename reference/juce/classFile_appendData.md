#### appendData()


 bool File::appendData ( const void \* dataToAppend, 
 
 size\_t numberOfBytes ) const 

Appends a block of binary data to the end of the file.This will try to write the given buffer to the end of the file.Returnsfalse if it can't write to the file for some reason