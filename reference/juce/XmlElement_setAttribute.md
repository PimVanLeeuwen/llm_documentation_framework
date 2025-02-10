#### setAttribute() [3/3]


 void XmlElement::setAttribute ( const Identifier & attributeName, 
 
 double newValue ) 

Adds a named attribute to the element, setting it to a floatingpoint value.If the element already contains an attribute with this name, it's value will be updated to the new value. If there's no such attribute yet, a new one will be added.Note that there are other setAttribute() methods that take integers, doubles, etc. to make it easy to store numbers.Parameters

 attributeName the name of the attribute to set 
 
 newValue the value to set it to