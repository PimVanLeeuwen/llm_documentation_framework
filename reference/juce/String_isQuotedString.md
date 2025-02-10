#### isQuotedString()


 bool String::isQuotedString ( ) const 
 

Checks whether the string might be in quotation marks.Returnstrue if the string begins with a quote character (either a double or single quote). It is also true if there is whitespace before the quote, but it doesn't check the end of the string. 
See alsounquoted, quoted