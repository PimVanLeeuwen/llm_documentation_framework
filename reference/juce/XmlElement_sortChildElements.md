#### sortChildElements()


template<class ElementComparator > 

 void XmlElement::sortChildElements ( ElementComparator & comparator, 
 
 bool retainOrderOfEquivalentItems = false ) 

Sorts the child elements using a comparator.This will use a comparator object to sort the elements into order. The object passed must have a method of the form:int compareElements (const XmlElement\* first, const XmlElement\* second);
..and this method must return:a value of < 0 if the first comes before the seconda value of 0 if the two objects are equivalenta value of > 0 if the second comes before the firstTo improve performance, the compareElements() method can be declared as static or const.Parameters

 comparator the comparator to use for comparing elements. 
 
 retainOrderOfEquivalentItems if this is true, then items which the comparator says are equivalent will be kept in the order in which they currently appear in the array. This is slower to perform, but may be important in some cases. If it's false, a faster algorithm is used, but equivalent elements may be rearranged.