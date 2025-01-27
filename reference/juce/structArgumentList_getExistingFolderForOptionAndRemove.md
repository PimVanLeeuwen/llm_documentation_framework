#### getExistingFolderForOptionAndRemove()


 File ArgumentList::getExistingFolderForOptionAndRemove ( StringRef option ) 
 

Looks for a filename argument using getFileForOption() and fails with a suitable error if the file isn't a folder that exists.This works like getExistingFolderForOption() but also removes the option argument (and any value arguments) from the list if they are found.

Member Data Documentation