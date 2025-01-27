#### substring() [2/2]


 String String::substring ( int startIndex ) const 
 

Returns a section of the string, starting from a given position.Parameters

 startIndex the first character to include. If this is beyond the end of the string, an empty string is returned. If it is zero or less, the whole string is returned. 
 



Returnsthe substring from startIndex up to the end of the string 
See alsodropLastCharacters, getLastCharacters, fromFirstOccurrenceOf, upToFirstOccurrenceOf, fromLastOccurrenceOf