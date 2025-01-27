#### getFileForOption()


 File ArgumentList::getFileForOption ( StringRef option ) const 
 

Looks for the value of argument using getValueForOption() and tries to parse that value as a file.If the option isn't found, or if the value can't be parsed as a filename, it will throw an error.