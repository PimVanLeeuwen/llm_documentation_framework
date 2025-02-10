#### fromFirstOccurrenceOf()


 String String::fromFirstOccurrenceOf ( StringRef substringToStartFrom, 
 
 bool includeSubStringInResult, 
 bool ignoreCase ) const 

Returns a section of the string starting from a given substring.This will search for the first occurrence of the given substring, and return the section of the string starting from the point where this is found (optionally not including the substring itself).e.g. for the string "123456", fromFirstOccurrenceOf ("34", true) would return "3456", and fromFirstOccurrenceOf ("34", false) would return "56".If the substring isn't found, the method will return an empty string.If ignoreCase is true, the comparison will be caseinsensitive.See alsoupToFirstOccurrenceOf, fromLastOccurrenceOf