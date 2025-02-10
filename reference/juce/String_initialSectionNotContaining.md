#### initialSectionNotContaining()


 String String::initialSectionNotContaining ( StringRef charactersToStopAt ) const 
 

Returns a section from the start of the string that only contains a certain set of characters.This returns the leftmost section of the string, up to (and not including) the first character that occurs in the string passed in. (If none of the specified characters are found in the string, the return value will just be the original string).