#### addNullTerminatedArray()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 
template<typename Type > 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::addNullTerminatedArray ( const Type \*const \* elementsToAdd ) 
 

Adds elements from a nullterminated array of pointers to the end of this array.Parameters

 elementsToAdd an array of pointers to some kind of object from which elements can be constructed. This array must be terminated by a nullptr 
 



See alsoaddArray References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::addArray().