#### addChildElement()


 void XmlElement::addChildElement ( XmlElement \* newChildElement ) noexcept 
 

Appends an element to this element's list of children.Child elements are deleted automatically when their parent is deleted, so make sure the object that you pass in will not be deleted by anything else, and make sure it's not already the child of another element.Note that due to the XmlElement using a singlylinkedlist, prependChildElement() is an O(1) operation, but addChildElement() is an O(N) operation so if you're adding large number of elements, you may prefer to do so in reverse order!See alsogetFirstChildElement, getNextElement, getNumChildElements, getChildElement, removeChildElement