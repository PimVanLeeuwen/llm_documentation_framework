#### removeLast()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::removeLast ( int howManyToRemove = 1 ) 
 

Removes the last n elements from the array.Parameters

 howManyToRemove how many elements to remove from the end of the array 
 



See alsoremove, removeFirstMatchingValue, removeAllInstancesOf, removeRange References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock(), and jassert.