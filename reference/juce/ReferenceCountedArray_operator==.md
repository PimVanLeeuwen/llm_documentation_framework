#### operator==()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 bool ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::operator== ( const ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse > & other ) const noexcept 
 

Compares this array to another one.Returnstrue only if the other array contains the same objects in the same order References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().Referenced by ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::operator!=().