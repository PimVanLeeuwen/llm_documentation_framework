#### set()


template<typename KeyType , typename ValueType , class HashFunctionType = DefaultHashFunctions, class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::set ( KeyTypeParameter newKey, 
 
 ValueTypeParameter newValue ) 

Adds or replaces an element in the hashmap.If there's already an item with the given key, this will replace its value. Otherwise, a new item will be added to the map.References HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getReference().