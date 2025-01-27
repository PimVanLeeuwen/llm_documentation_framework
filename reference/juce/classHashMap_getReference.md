#### getReference()


template<typename KeyType , typename ValueType , class HashFunctionType = DefaultHashFunctions, class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ValueType & HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getReference ( KeyTypeParameter keyToLookFor ) 
 

Returns a reference to the value corresponding to a given key.If the map doesn't contain the key, a default instance of the value type is added to the map and a reference to this is returned.Parameters

 keyToLookFor the key of the item being requested 
 


References HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getLock(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getNumSlots(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getUnchecked(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::remapTable(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::set().Referenced by HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::set().