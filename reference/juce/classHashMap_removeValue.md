#### removeValue()


template<typename KeyType , typename ValueType , class HashFunctionType = DefaultHashFunctions, class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::removeValue ( ValueTypeParameter valueToRemove ) 
 

Removes all items with the given value.References HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getLock(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getNumSlots(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getUnchecked(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::set().