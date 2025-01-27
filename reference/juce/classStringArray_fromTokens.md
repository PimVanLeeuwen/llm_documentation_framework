#### fromTokens() [2/2]


 static StringArray StringArray::fromTokens ( StringRef stringToTokenise, StringRef breakCharacters, StringRef quoteCharacters ) static 
 

Returns an array containing the tokens in a given string.This will tokenise the given string using the breakCharacters string to define the token delimiters, and will return the parsed tokens as an array.Parameters

 stringToTokenise the string to tokenise 
 
 breakCharacters a string of characters, any of which will be considered to be a token delimiter. 
 quoteCharacters if this string isn't empty, it defines a set of characters which are treated as quotes. Any text occurring between quotes is not broken up into tokens. 



See alsoaddTokens