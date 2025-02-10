#### addSorted()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 
template<class ElementComparator > 

 int ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::addSorted ( ElementComparator & comparator, ObjectClass \* newObject ) noexcept 
 

Inserts a new object into the array assuming that the array is sorted.This will use a comparator to find the position at which the new object should go. If the array isn't sorted, the behaviour of this method will be unpredictable.Parameters

 comparator the comparator object to use to compare the elements see the sort() method for details about this object's form 
 
 newObject the new object to insert to the array 



Returnsthe index at which the new object was added 
See alsoadd, sort References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock(), and ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::insert().