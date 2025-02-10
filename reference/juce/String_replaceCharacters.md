#### replaceCharacters()


 String String::replaceCharacters ( StringRef charactersToReplace, 
 
 StringRef charactersToInsertInstead ) const 

Replaces a set of characters with another set.Returns a string in which each character from charactersToReplace has been replaced by the character at the equivalent position in newCharacters (so the two strings passed in must be the same length).e.g. replaceCharacters ("abc", "def") replaces 'a' with 'd', 'b' with 'e', etc.Note that this is a const method, and won't affect the string itself.