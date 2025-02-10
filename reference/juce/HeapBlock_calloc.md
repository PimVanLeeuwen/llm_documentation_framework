#### calloc()


template<class ElementType , bool throwOnFailure = false> 
template<typename SizeType > 

 void HeapBlock< ElementType, throwOnFailure >::calloc ( SizeType newNumElements, 
 
 const size\_t elementSize = sizeof (ElementType) ) 

Allocates a specified amount of memory and clears it.This does the same job as the malloc() method, but clears the memory that it allocates.