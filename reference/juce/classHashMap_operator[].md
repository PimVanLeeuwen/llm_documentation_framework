#### operator[]()


template<typename KeyType , typename ValueType , class HashFunctionType = DefaultHashFunctions, class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ValueType HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::operator[] ( KeyTypeParameter keyToLookFor ) const 
 

Returns the value corresponding to a given key.If the map doesn't contain the key, a default instance of the value type is returned.Parameters

 keyToLookFor the key of the item being requested 
 


References HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getLock().