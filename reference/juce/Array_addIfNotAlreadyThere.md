#### addIfNotAlreadyThere()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 bool Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::addIfNotAlreadyThere ( ParameterType newElement ) 
 

Appends a new element at the end of the array as long as the array doesn't already contain it.If the array already contains an element that matches the one passed in, nothing will be done.Parameters

 newElement the new object to add to the array 
 



Returnstrue if the element was added to the array; false otherwise. References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::add(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::contains(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().