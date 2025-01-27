#### getExistingFileForOptionAndRemove()


 File ArgumentList::getExistingFileForOptionAndRemove ( StringRef option ) 
 

Looks for a file argument using getFileForOption() and fails with a suitable error if the file doesn't exist.This works like getExistingFileForOption() but also removes the option argument (and any value arguments) from the list if they are found.