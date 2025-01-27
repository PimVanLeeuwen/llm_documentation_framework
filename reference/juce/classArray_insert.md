#### insert()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::insert ( int indexToInsertAt, 
 
 ParameterType newElement ) 

Inserts a new element into the array at a given position.If the index is less than 0 or greater than the size of the array, the element will be added to the end of the array. Otherwise, it will be inserted into the array, moving all the later elements along to make room.Parameters

 indexToInsertAt the index at which the new element should be inserted (pass in 1 to add it to the end) 
 
 newElement the new object to add to the array 



See alsoadd, addSorted, addUsingDefaultSort, set References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().Referenced by Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::addSorted(), and SparseSet< Type >::removeRange().