#### addTokens() [2/2]


 int StringArray::addTokens ( StringRef stringToTokenise, 
 
 StringRef breakCharacters, 
 StringRef quoteCharacters ) 

Breaks up a string into tokens and adds them to this array.This will tokenise the given string (using the string passed in to define the token delimiters), and will add these tokens to the end of the array.Parameters

 stringToTokenise the string to tokenise 
 
 breakCharacters a string of characters, any of which will be considered to be a token delimiter. 
 quoteCharacters if this string isn't empty, it defines a set of characters which are treated as quotes. Any text occurring between quotes is not broken up into tokens. 



Returnsthe number of tokens added 
See alsofromTokens