#### setValue() [2/2]


 void PropertySet::setValue ( StringRef keyName, 
 
 const XmlElement \* xml ) 

Sets a named property to an XML element.Parameters

 keyName the name of the property to set. (This mustn't be an empty string) 
 
 xml the new element to set it to. If this is a nullptr, the value will be set to an empty string 



See alsogetXmlValue