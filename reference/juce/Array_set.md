#### set()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::set ( int indexToChange, 
 
 ParameterType newValue ) 

Replaces an element with a new value.If the index is less than zero, this method does nothing. If the index is beyond the end of the array, the item is added to the end of the array.Parameters

 indexToChange the index whose value you want to change 
 
 newValue the new value to set for this index. 



See alsoadd, insert References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock(), and jassertfalse.Referenced by HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::clear(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getReference(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::remapTable(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::remove(), and HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::removeValue().