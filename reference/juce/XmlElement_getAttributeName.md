#### getAttributeName()


 const String & XmlElement::getAttributeName ( int attributeIndex ) const noexcept 
 

Returns the name of one of the elements attributes.E.g. for an element such as <MOOSE legs="4" antlers="2">, then getAttributeName (1) would return "antlers".See alsogetAttributeValue, getStringAttribute