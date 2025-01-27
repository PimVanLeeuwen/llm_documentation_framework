#### malloc()


template<class ElementType , bool throwOnFailure = false> 
template<typename SizeType > 

 void HeapBlock< ElementType, throwOnFailure >::malloc ( SizeType newNumElements, 
 
 size\_t elementSize = sizeof (ElementType) ) 

Allocates a specified amount of memory.This uses the normal malloc to allocate an amount of memory for this object. Any previously allocated memory will be freed by this method.The number of bytes allocated will be (newNumElements \* elementSize). Normally you wouldn't need to specify the second parameter, but it can be handy if you need to allocate a size in bytes rather than in terms of the number of elements.The data that is allocated will be freed when this object is deleted, or when you call free() or any of the allocation methods.Referenced by dsp::FIR::Filter< SampleType >::reset().