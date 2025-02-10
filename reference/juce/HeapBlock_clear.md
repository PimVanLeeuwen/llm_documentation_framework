#### clear()


template<class ElementType , bool throwOnFailure = false> 
template<typename SizeType > 

 void HeapBlock< ElementType, throwOnFailure >::clear ( SizeType numElements ) noexcept 
 

This fills the block with zeros, up to the number of elements specified.Since the block has no way of knowing its own size, you must make sure that the number of elements you specify doesn't exceed the allocated size.References zeromem().Referenced by AudioBuffer< Type >::setSize().