#### contains()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 bool Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::contains ( ParameterType elementToLookFor ) const 
 

Returns true if the array contains at least one occurrence of an object.Parameters

 elementToLookFor the value or object to look for 
 



Returnstrue if the item is found References exactlyEqual(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().Referenced by Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::addIfNotAlreadyThere(), and SelectedItemSet< SelectableItemType >::isSelected().