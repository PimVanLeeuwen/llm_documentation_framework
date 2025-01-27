#### parse()


 static Expression Expression::parse ( String::CharPointerType & stringToParse, String & parseError ) static 
 

Returns an Expression which parses a string from a character pointer, and updates the pointer to indicate where it finished.The pointer is incremented so that on return, it indicates the character that follows the end of the expression that was parsed.If there's a syntax error in parsing, the parseError argument will be set to a description of the problem.