#### removeCharacters()


 String String::removeCharacters ( StringRef charactersToRemove ) const 
 

Returns a version of this string with a set of characters removed.This will return a copy of this string, omitting any characters which are found in the string passedin.e.g. for "1122334455", removeCharacters ("432") would return "1155"Note that this is a const method, and won't alter the string itself.