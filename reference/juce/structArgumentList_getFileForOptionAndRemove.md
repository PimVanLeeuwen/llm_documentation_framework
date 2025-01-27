#### getFileForOptionAndRemove()


 File ArgumentList::getFileForOptionAndRemove ( StringRef option ) 
 

Looks for the value of argument using getValueForOption() and tries to parse that value as a file.This works like getFileForOption() but also removes the option argument (and any value arguments) from the list if they are found.