#### getChildElementAllSubText()


 String XmlElement::getChildElementAllSubText ( StringRef childTagName, 
 
 const String & defaultReturnValue ) const 

Returns all the subtext of a named child element.If there is a child element with the given tag name, this will return all of its subtext (by calling getAllSubText() on it). If there is no such child element, this will return the default string passedin.See alsogetAllSubText