#### getValueForOption()


 String ArgumentList::getValueForOption ( StringRef option ) const 
 

Looks for a given argument and returns either its assigned value (for long options) or the string that follows it (for short options).The option can also be a list of different versions separated by pipes, e.g. "helph" If it finds a long option, it will look for an assignment with a '=' sign, e.g. "file=foo.txt", and will return the string following the '='. If there's no '=', it will return an empty string. If it finds a short option, it will attempt to return the argument that follows it, unless it's another option. If the argument isn't found, this returns an empty string.