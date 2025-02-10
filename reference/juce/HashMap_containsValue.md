#### containsValue()


template<typename KeyType , typename ValueType , class HashFunctionType = DefaultHashFunctions, class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 bool HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::containsValue ( ValueTypeParameter valueToLookFor ) const 
 

Returns true if the hash contains at least one occurrence of a given value.References HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getLock(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getNumSlots(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getUnchecked().