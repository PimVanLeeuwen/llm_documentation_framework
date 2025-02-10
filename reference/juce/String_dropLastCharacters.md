#### dropLastCharacters()


 String String::dropLastCharacters ( int numberToDrop ) const 
 

Returns a version of this string with a number of characters removed from the end.Parameters

 numberToDrop the number of characters to drop from the end of the string. If this is greater than the length of the string, an empty string will be returned. If zero or less, the original string will be returned. 
 



See alsosubstring, fromFirstOccurrenceOf, upToFirstOccurrenceOf, fromLastOccurrenceOf, getLastCharacter