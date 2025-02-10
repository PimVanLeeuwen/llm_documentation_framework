#### getDocumentElement()


 std::unique\_ptr< XmlElement > XmlDocument::getDocumentElement ( bool onlyReadOuterDocumentElement = false ) 
 

Creates an XmlElement object to represent the main document node.This method will do the actual parsing of the text, and if there's a parse error, it may returns nullptr (and you can find out the error using the getLastParseError() method).See also the parse() methods, which provide a shorthand way to quickly parse a file or string.Parameters

 onlyReadOuterDocumentElement if true, the parser will only read the first section of the file, and will only return the outer document element this allows quick checking of large files to see if they contain the correct type of tag, without having to parse the entire file 
 



Returnsa new XmlElement, or nullptr if there was an error. 
See alsogetLastParseError, getDocumentElementIfTagMatches