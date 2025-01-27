#### addEscapeChars()


 static String URL::addEscapeChars ( const String & stringToAddEscapeCharsTo, bool isParameter, bool roundBracketsAreLegal = true ) static 
 

Adds escape sequences to a string to encode any characters that aren't legal in a URL.E.g. any spaces will be replaced with "%20".This is the opposite of removeEscapeChars().Parameters

 stringToAddEscapeCharsTo the string to escape. 
 
 isParameter if true then the string is going to be used as a parameter, so it also encodes '$' and ',' (which would otherwise be legal in a URL. 
 roundBracketsAreLegal technically round brackets are ok in URLs, however, some servers (like AWS) also want round brackets to be escaped. 



See alsoremoveEscapeChars