#### sort()


template<typename ElementComparator > 

 void ValueTree::sort ( ElementComparator & comparator, 
 
 UndoManager \* undoManager, 
 bool retainOrderOfEquivalentItems ) 

This method uses a comparator object to sort the tree's children into order.The object provided must have a method of the form:int compareElements (const ValueTree& first, const ValueTree& second);
..and this method must return:a value of < 0 if the first comes before the seconda value of 0 if the two objects are equivalenta value of > 0 if the second comes before the firstTo improve performance, the compareElements() method can be declared as static or const.Parameters

 comparator the comparator to use for comparing elements. 
 
 undoManager optional UndoManager for storing the changes 
 retainOrderOfEquivalentItems if this is true, then items which the comparator says are equivalent will be kept in the order in which they currently appear in the array. This is slower to perform, but may be important in some cases. If it's false, a faster algorithm is used, but equivalent elements may be rearranged. 


References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::sort().