#### parse() [2/2]


 static std::unique\_ptr< XmlElement > XmlDocument::parse ( const String & xmlData ) static 
 

A handy static method that parses some XML data.This is a shortcut for creating an XmlDocument object and calling getDocumentElement() on it.Returnsa new XmlElement, or nullptr if there was an error.