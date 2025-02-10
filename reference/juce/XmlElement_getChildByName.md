#### getChildByName()


 XmlElement \* XmlElement::getChildByName ( StringRef tagNameToLookFor ) const noexcept 
 

Returns the first subelement with a given tagname.Parameters

 tagNameToLookFor the tag name of the element you want to find 
 



Returnsthe first element with this tag name, or nullptr if none is found 
See alsogetNextElement, isTextElement, getChildElement, getChildByAttribute