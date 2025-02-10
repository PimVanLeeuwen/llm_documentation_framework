#### getDoubleAttribute()


 double XmlElement::getDoubleAttribute ( StringRef attributeName, 
 
 double defaultReturnValue = 0.0 ) const 

Returns the value of a named attribute as floatingpoint.This will try to find the attribute and convert it to a double (using the String::getDoubleValue() method).Parameters

 attributeName the name of the attribute to look up 
 
 defaultReturnValue a value to return if the element doesn't have an attribute with this name 



See alsosetAttribute