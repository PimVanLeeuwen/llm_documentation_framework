#### allocate()


template<class ElementType , bool throwOnFailure = false> 
template<typename SizeType > 

 void HeapBlock< ElementType, throwOnFailure >::allocate ( SizeType newNumElements, 
 
 bool initialiseToZero ) 

Allocates a specified amount of memory and optionally clears it.This does the same job as either malloc() or calloc(), depending on the initialiseToZero parameter.Referenced by AudioBuffer< Type >::setSize().