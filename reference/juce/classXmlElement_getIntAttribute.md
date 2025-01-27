#### getIntAttribute()


 int XmlElement::getIntAttribute ( StringRef attributeName, 
 
 int defaultReturnValue = 0 ) const 

Returns the value of a named attribute as an integer.This will try to find the attribute and convert it to an integer (using the String::getIntValue() method).Parameters

 attributeName the name of the attribute to look up 
 
 defaultReturnValue a value to return if the element doesn't have an attribute with this name 



See alsosetAttribute