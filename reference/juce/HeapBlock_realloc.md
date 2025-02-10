#### realloc()


template<class ElementType , bool throwOnFailure = false> 
template<typename SizeType > 

 void HeapBlock< ElementType, throwOnFailure >::realloc ( SizeType newNumElements, 
 
 size\_t elementSize = sizeof (ElementType) ) 

Reallocates a specified amount of memory.The semantics of this method are the same as malloc() and calloc(), but it uses realloc() to keep as much of the existing data as possible.