#### swapWith()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 
template<class OtherSetType > 

 void SortedSet< ElementType, TypeOfCriticalSectionToUse >::swapWith ( OtherSetType & otherSet ) noexcept 
 

This swaps the contents of this array with those of another array.If you need to exchange two arrays, this is vastly quicker than using copybyvalue because it just swaps their internal pointers.