#### fromLastOccurrenceOf()


 String String::fromLastOccurrenceOf ( StringRef substringToFind, 
 
 bool includeSubStringInResult, 
 bool ignoreCase ) const 

Returns a section of the string starting from the last occurrence of a given substring.Similar to fromFirstOccurrenceOf(), but using the last occurrence of the substring, and unlike fromFirstOccurrenceOf(), if the substring isn't found, this method will return the whole of the original string.See alsofromFirstOccurrenceOf, upToLastOccurrenceOf