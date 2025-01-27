#### findParentElementOf()


 XmlElement \* XmlElement::findParentElementOf ( const XmlElement \* childToSearchFor ) noexcept 
 

Recursively searches all subelements of this one, looking for an element which is the direct parent of the specified element.Because elements don't store a pointer to their parent, if you have one and need to find its parent, the only way to do so is to exhaustively search the whole tree for it.If the given child is found somewhere in this element's hierarchy, then this method will return its parent. If not, it will return nullptr.