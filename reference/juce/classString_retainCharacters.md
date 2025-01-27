#### retainCharacters()


 String String::retainCharacters ( StringRef charactersToRetain ) const 
 

Returns a version of this string that only retains a fixed set of characters.This will return a copy of this string, omitting any characters which are not found in the string passedin.e.g. for "1122334455", retainCharacters ("432") would return "223344"Note that this is a const method, and won't alter the string itself.