#### addArray() [2/2]


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 
template<typename OtherArrayType > 

 void OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::addArray ( const std::initializer\_list< OtherArrayType > & items ) 
 

Adds elements from another array to the end of this array.References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().