#### swapWith()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 
template<class OtherArrayType > 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::swapWith ( OtherArrayType & otherArray ) noexcept 
 

This swaps the contents of this array with those of another array.If you need to exchange two arrays, this is vastly quicker than using copybyvalue because it just swaps their internal pointers.References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().Referenced by Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::operator=(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::remapTable(), and HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::swapWith().