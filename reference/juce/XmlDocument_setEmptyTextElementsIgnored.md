#### setEmptyTextElementsIgnored()


 void XmlDocument::setEmptyTextElementsIgnored ( bool shouldBeIgnored ) noexcept 
 

Sets a flag to change the treatment of empty text elements.If this is true (the default state), then any text elements that contain only whitespace characters will be ignored during parsing. If you need to catch whitespaceonly text, then you should set this to false before calling the getDocumentElement() method.