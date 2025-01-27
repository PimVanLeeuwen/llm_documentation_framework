#### fromString()


template<typename ValueType > 

 static Rectangle Rectangle< ValueType >::fromString ( StringRef stringVersion ) static 
 

Parses a string containing a rectangle's details.The string should contain 4 numeric tokens, in the form "x y width height". They can be comma or whitespace separated.This method is intended to go with the toString() method, to form an easy way of saving/loading rectangles as strings.See alsotoString References StringArray::addTokens(), CharPointer\_UTF8::findEndOfWhitespace(), and StringRef::text.