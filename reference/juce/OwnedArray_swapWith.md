#### swapWith()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 
template<class OtherArrayType > 

 void OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::swapWith ( OtherArrayType & otherArray ) noexcept 
 

This swaps the contents of this array with those of another array.If you need to exchange two arrays, this is vastly quicker than using copybyvalue because it just swaps their internal pointers.References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().