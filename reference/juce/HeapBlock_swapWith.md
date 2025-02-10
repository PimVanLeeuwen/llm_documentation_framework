#### swapWith()


template<class ElementType , bool throwOnFailure = false> 
template<bool otherBlockThrows> 

 void HeapBlock< ElementType, throwOnFailure >::swapWith ( HeapBlock< ElementType, otherBlockThrows > & other ) noexcept 
 

Swaps this object's data with the data of another HeapBlock.The two objects simply exchange their data pointers.Referenced by AudioBuffer< Type >::setSize().