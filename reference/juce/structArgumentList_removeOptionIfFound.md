#### removeOptionIfFound()


 bool ArgumentList::removeOptionIfFound ( StringRef option ) 
 

Returns true if the given string matches one of the arguments, and also removes the argument from the list if found.The option can also be a list of different versions separated by pipes, e.g. "helph"See alsocontainsOption