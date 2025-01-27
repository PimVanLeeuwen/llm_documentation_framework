#### indexOf()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 int Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::indexOf ( ParameterType elementToLookFor ) const 
 

Finds the index of the first element which matches the value passed in.This will search the array for the given object, and return the index of its first occurrence. If the object isn't found, the method will return 1.Parameters

 elementToLookFor the value or object to look for 
 



Returnsthe index of the object, or 1 if it's not found References exactlyEqual(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().Referenced by SelectedItemSet< SelectableItemType >::deselect().