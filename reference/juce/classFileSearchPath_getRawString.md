#### getRawString()


 String FileSearchPath::getRawString ( int index ) const 
 

Returns the unaltered text of the folder at the specified index.Unlike operator[], this function returns the exact text that was entered. It does not attempt to convert the path into an absolute path.This may be useful if the directory string is expected to understand environment variables or other placeholders that the File constructor doesn't necessarily understand.See alsooperator[]