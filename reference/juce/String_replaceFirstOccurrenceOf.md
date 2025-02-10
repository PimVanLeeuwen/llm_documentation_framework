#### replaceFirstOccurrenceOf()


 String String::replaceFirstOccurrenceOf ( StringRef stringToReplace, 
 
 StringRef stringToInsertInstead, 
 bool ignoreCase = false ) const 

Replaces the first occurrence of a substring with another string.Returns a copy of this string, with the first occurrence of stringToReplace swapped for stringToInsertInstead.Note that this is a const method, and won't alter the string itself.