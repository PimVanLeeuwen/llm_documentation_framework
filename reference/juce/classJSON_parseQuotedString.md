#### parseQuotedString()


 static Result JSON::parseQuotedString ( String::CharPointerType & text, var & result ) static 
 

Parses a quoted stringliteral in JSON format, returning the unescaped result in the result parameter, and an error message in case the content was illegal.This advances the text parameter, leaving it positioned after the closing quote.