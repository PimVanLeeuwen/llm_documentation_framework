#### indexOfWholeWord()


 int String::indexOfWholeWord ( StringRef wordToLookFor ) const noexcept 
 

Finds an instance of another substring if it exists as a distinct word.Returnsif the string contains this word, surrounded by nonalphanumeric characters, then this will return the index of the start of the substring. If it isn't found, then it will return 1 
See alsoindexOfWholeWordIgnoreCase, containsWholeWord