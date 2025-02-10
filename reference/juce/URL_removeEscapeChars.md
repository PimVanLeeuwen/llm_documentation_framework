#### removeEscapeChars()


 static String URL::removeEscapeChars ( const String & stringToRemoveEscapeCharsFrom ) static 
 

Replaces any escape character sequences in a string with their original character codes.E.g. any instances of "%20" will be replaced by a space.This is the opposite of addEscapeChars().See alsoaddEscapeChars