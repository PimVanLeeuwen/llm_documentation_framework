#### getNumberOfChildFiles()


 int File::getNumberOfChildFiles ( int whatToLookFor, 
 
 const String & wildCardPattern = "\*" ) const 

Searches inside a directory and counts how many files match a wildcard pattern.Assuming that this file is a directory, this method will search it for either files or subdirectories whose names match a filename pattern, and will return the number of matches found.This isn't a recursive call, and will only search this directory, not its children.Parameters

 whatToLookFor a value from the TypesOfFileToFind enum, specifying whether to count files, directories, or both. If the ignoreHiddenFiles flag is also added to this value, hidden files won't be counted 
 
 wildCardPattern the filename pattern to search for, e.g. "\*.txt" 



Returnsthe number of matches found
See alsofindChildFiles, RangedDirectoryIterator