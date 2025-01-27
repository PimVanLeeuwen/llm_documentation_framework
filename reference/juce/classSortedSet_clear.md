#### clear()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void SortedSet< ElementType, TypeOfCriticalSectionToUse >::clear ( ) noexcept 
 

Removes all elements from the set.This will remove all the elements, and free any storage that the set is using. To clear it without freeing the storage, use the clearQuick() method instead.See alsoclearQuick