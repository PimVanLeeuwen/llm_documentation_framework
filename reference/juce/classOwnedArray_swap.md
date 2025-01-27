#### swap()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::swap ( int index1, int index2 ) noexcept 
 

Swaps a pair of objects in the array.If either of the indexes passed in is outofrange, nothing will happen, otherwise the two objects at these positions will be exchanged.References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().