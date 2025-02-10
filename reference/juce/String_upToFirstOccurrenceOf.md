#### upToFirstOccurrenceOf()


 String String::upToFirstOccurrenceOf ( StringRef substringToEndWith, 
 
 bool includeSubStringInResult, 
 bool ignoreCase ) const 

Returns the start of this string, up to the first occurrence of a substring.This will search for the first occurrence of a given substring, and then return a copy of the string, up to the position of this substring, optionally including or excluding the substring itself in the result.e.g. for the string "123456", upTo ("34", false) would return "12", and upTo ("34", true) would return "1234".If the substring isn't found, this will return the whole of the original string.See alsoupToLastOccurrenceOf, fromFirstOccurrenceOf