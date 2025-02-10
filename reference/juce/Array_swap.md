#### swap()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::swap ( int index1, 
 
 int index2 ) 

Swaps over two elements in the array.This swaps over the elements found at the two indexes passed in. If either index is outofrange, this method will do nothing.Parameters

 index1 index of one of the elements to swap 
 
 index2 index of the other element to swap 


References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().