#### parse() [4/4]


 static var JSON::parse ( InputStream & input ) static 
 

Attempts to parse some JSONformatted text from a stream, and returns the result as a var object.Note that this is just a shortcut for reading the entire stream into a string and parsing the result.If the parsing fails, this simply returns var() if you need to find out more detail about the parse error, use the alternative parse() method which returns a Result.