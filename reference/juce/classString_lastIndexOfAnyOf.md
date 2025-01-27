#### lastIndexOfAnyOf()


 int String::lastIndexOfAnyOf ( StringRef charactersToLookFor, bool ignoreCase = false ) const noexcept 
 

Returns the index of the last character in this string that matches one of the characters passedin to this method.This scans the string backwards, starting from its end, and if it finds a character that appears in the string charactersToLookFor, it returns its index.If none of these characters are found, it returns 1.If ignoreCase is true, the comparison will be caseinsensitive.See alsolastIndexOf, indexOfAnyOf