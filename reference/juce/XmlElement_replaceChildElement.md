#### replaceChildElement()


 bool XmlElement::replaceChildElement ( XmlElement \* currentChildElement, XmlElement \* newChildNode ) noexcept 
 

Replaces one of this element's children with another node.If the current element passedin isn't actually a child of this element, this will return false and the new one won't be added. Otherwise, the existing element will be deleted, replaced with the new one, and it will return true.