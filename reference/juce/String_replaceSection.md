#### replaceSection()


 String String::replaceSection ( int startIndex, 
 
 int numCharactersToReplace, 
 StringRef stringToInsert ) const 

Replaces a subsection of the string with another string.This will return a copy of this string, with a set of characters from startIndex to startIndex + numCharsToReplace removed, and with a new string inserted in their place.Note that this is a const method, and won't alter the string itself.Parameters

 startIndex the first character to remove. If this is beyond the bounds of the string, it will be constrained to a valid range. 
 
 numCharactersToReplace the number of characters to remove. If zero or less, no characters will be taken out. 
 stringToInsert the new string to insert at startIndex after the characters have been removed.