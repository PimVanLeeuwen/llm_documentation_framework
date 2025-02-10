#### getUnchecked()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 ElementType Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getUnchecked ( int index ) const 
 

Returns one of the elements in the array, without checking the index passed in.Unlike the operator[] method, this will try to return an element without checking that the index is within the bounds of the array, so should only be used when you're confident that it will always be a valid index.Parameters

 index the index of the element being requested (0 is the first element in the array) 
 



See alsooperator[], getFirst, getLast References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().Referenced by HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::clear(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::containsValue(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getReference(), dsp::LookupTable< FloatType >::getUnchecked(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::Iterator::next(), dsp::Polynomial< FloatingType >::operator()(), dsp::Polynomial< FloatingType >::operator[](), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::remapTable(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::remove(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::removeValue(), and SelectedItemSet< SelectableItemType >::selectOnly().