#### removeValueForOption()


 String ArgumentList::removeValueForOption ( StringRef option ) 
 

Looks for a given argument and returns either its assigned value (for long options) or the string that follows it (for short options).This works like getValueForOption() but also removes the option argument (and any value arguments) from the list if they are found.