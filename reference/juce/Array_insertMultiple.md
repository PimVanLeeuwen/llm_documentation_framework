#### insertMultiple()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::insertMultiple ( int indexToInsertAt, 
 
 ParameterType newElement, 
 int numberOfTimesToInsertIt ) 

Inserts multiple copies of an element into the array at a given position.If the index is less than 0 or greater than the size of the array, the element will be added to the end of the array. Otherwise, it will be inserted into the array, moving all the later elements along to make room.Parameters

 indexToInsertAt the index at which the new element should be inserted 
 
 newElement the new object to add to the array 
 numberOfTimesToInsertIt how many copies of the value to insert 



See alsoinsert, add, addSorted, set References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().Referenced by HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::HashMap(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::remapTable(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::resize().