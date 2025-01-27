#### operator=() [2/2]


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 
template<class OtherObjectClass , class OtherCriticalSection > 

 OwnedArray & OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::operator= ( OwnedArray< OtherObjectClass, OtherCriticalSection > && other ) noexcept 
 

Converting move assignment operator.References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().