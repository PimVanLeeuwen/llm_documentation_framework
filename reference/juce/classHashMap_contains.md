#### contains()


template<typename KeyType , typename ValueType , class HashFunctionType = DefaultHashFunctions, class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 bool HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::contains ( KeyTypeParameter keyToLookFor ) const 
 

Returns true if the map contains an item with the specified key.References HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getLock().