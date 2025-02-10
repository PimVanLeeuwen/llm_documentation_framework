#### getNextElementWithTagName()


 XmlElement \* XmlElement::getNextElementWithTagName ( StringRef requiredTagName ) const 
 

Returns the next of this element's siblings which has the specified tag name.This is like getNextElement(), but will scan through the list until it finds an element with the given tag name.See alsogetNextElement, getChildIterator