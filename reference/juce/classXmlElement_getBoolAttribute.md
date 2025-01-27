#### getBoolAttribute()


 bool XmlElement::getBoolAttribute ( StringRef attributeName, 
 
 bool defaultReturnValue = false ) const 

Returns the value of a named attribute as a boolean.This will try to find the attribute and interpret it as a boolean. To do this, it'll return true if the value is "1", "true", "y", etc, or false for other values.Parameters

 attributeName the name of the attribute to look up 
 
 defaultReturnValue a value to return if the element doesn't have an attribute with this name