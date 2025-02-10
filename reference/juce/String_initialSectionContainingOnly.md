#### initialSectionContainingOnly()


 String String::initialSectionContainingOnly ( StringRef permittedCharacters ) const 
 

Returns a section from the start of the string that only contains a certain set of characters.This returns the leftmost section of the string, up to (and not including) the first character that doesn't appear in the string passed in.