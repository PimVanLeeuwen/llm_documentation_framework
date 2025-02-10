#### getChildElement()


 XmlElement \* XmlElement::getChildElement ( int index ) const noexcept 
 

Returns the subelement at a certain index.It's not very efficient to iterate the subelements by index see getNextElement() for an example of how best to iterate.Returnsthe n'th child of this element, or nullptr if the index is outofrange 
See alsogetNextElement, isTextElement, getChildByName