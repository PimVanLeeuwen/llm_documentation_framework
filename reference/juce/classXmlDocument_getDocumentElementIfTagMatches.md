#### getDocumentElementIfTagMatches()


 std::unique\_ptr< XmlElement > XmlDocument::getDocumentElementIfTagMatches ( StringRef requiredTag ) 
 

Does an inexpensive check to see whether the outer element has the given tag name, and then does a full parse if it matches.If the tag is different, or the XML parse fails, this will return nullptr.