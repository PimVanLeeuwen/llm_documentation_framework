#### indexOfAnyOf()


 int String::indexOfAnyOf ( StringRef charactersToLookFor, int startIndex = 0, bool ignoreCase = false ) const noexcept 
 

Returns the index of the first character that matches one of the characters passedin to this method.This scans the string, beginning from the startIndex supplied, and if it finds a character that appears in the string charactersToLookFor, it returns its index.If none of these characters are found, it returns 1.If ignoreCase is true, the comparison will be caseinsensitive.See alsoindexOfChar, lastIndexOfAnyOf