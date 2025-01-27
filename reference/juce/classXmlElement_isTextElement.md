#### isTextElement()


 bool XmlElement::isTextElement ( ) const noexcept 
 

Returns true if this element is a section of text.Elements can either be an XML tag element or a section of text, so this is used to find out what kind of element this one is.See alsogetAllText, addTextElement, deleteAllTextElements