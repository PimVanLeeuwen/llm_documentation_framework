#### fromString()


 static var JSON::fromString ( StringRef ) static 
 

Parses a string that was created with the toString() method.This is slightly different to the parse() methods because they will reject primitive values and only accept array or object definitions, whereas this method will handle either.