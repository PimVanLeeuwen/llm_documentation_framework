#### begin()


template<typename KeyType , typename ValueType , class HashFunctionType = DefaultHashFunctions, class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 Iterator HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::begin ( ) const noexcept 
 

Returns a start iterator for the values in this tree.References HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::Iterator::next().