#### getChildByAttribute()


 XmlElement \* XmlElement::getChildByAttribute ( StringRef attributeName, StringRef attributeValue ) const noexcept 
 

Returns the first subelement which has an attribute that matches the given value.Parameters

 attributeName the name of the attribute to check 
 
 attributeValue the target value of the attribute 



Returnsthe first element with this attribute value, or nullptr if none is found 
See alsogetChildByName