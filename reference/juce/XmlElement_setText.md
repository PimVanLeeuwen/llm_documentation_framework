#### setText()


 void XmlElement::setText ( const String & newText ) 
 

Sets the text in a text element.Note that this is only a valid call if this element is a text element. If it's not, then no action will be performed. If you're trying to add text inside a normal element, you probably want to use addTextElement() instead.