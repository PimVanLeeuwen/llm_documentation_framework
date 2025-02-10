#### replace()


 String String::replace ( StringRef stringToReplace, 
 
 StringRef stringToInsertInstead, 
 bool ignoreCase = false ) const 

Replaces all occurrences of a substring with another string.Returns a copy of this string, with any occurrences of stringToReplace swapped for stringToInsertInstead.Note that this is a const method, and won't alter the string itself.