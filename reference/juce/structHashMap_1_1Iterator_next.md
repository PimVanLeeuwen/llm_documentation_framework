#### next()


template<typename KeyType , typename ValueType , class HashFunctionType = DefaultHashFunctions, class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 bool HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::Iterator::next ( ) noexcept 
 

Moves to the next item, if one is available.When this returns true, you can get the item's key and value using getKey() and getValue(). If it returns false, the iteration has finished and you should stop.References HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getNumSlots(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getUnchecked().Referenced by HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::begin(), and HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::Iterator::operator++().