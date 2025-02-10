#### insertChildElement()


 void XmlElement::insertChildElement ( XmlElement \* newChildElement, int indexToInsertAt ) noexcept 
 

Inserts an element into this element's list of children.Child elements are deleted automatically when their parent is deleted, so make sure the object that you pass in will not be deleted by anything else, and make sure it's not already the child of another element.Parameters

 newChildElement the element to add 
 
 indexToInsertAt the index at which to insert the new element if this is below zero, it will be added to the end of the list 



See alsoaddChildElement, insertChildElement