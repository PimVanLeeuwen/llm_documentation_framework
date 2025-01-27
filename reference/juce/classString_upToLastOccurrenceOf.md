#### upToLastOccurrenceOf()


 String String::upToLastOccurrenceOf ( StringRef substringToFind, 
 
 bool includeSubStringInResult, 
 bool ignoreCase ) const 

Returns the start of this string, up to the last occurrence of a substring.Similar to upToFirstOccurrenceOf(), but this finds the last occurrence rather than the first. If the substring isn't found, this will return the whole of the original string.See alsoupToFirstOccurrenceOf, fromFirstOccurrenceOf