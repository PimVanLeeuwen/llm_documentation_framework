#### addOrReplaceSorted()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 
template<class ElementComparator > 

 void ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::addOrReplaceSorted ( ElementComparator & comparator, ObjectClass \* newObject ) noexcept 
 

Inserts or replaces an object in the array, assuming it is sorted.This is similar to addSorted, but if a matching element already exists, then it will be replaced by the new one, rather than the new one being added as well.References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock(), ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::insert(), and ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::set().