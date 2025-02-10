#### clear()


template<typename KeyType , typename ValueType , class HashFunctionType = DefaultHashFunctions, class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::clear ( ) 
 

Removes all values from the map.Note that this will clear the content, but won't affect the number of slots (see remapTable and getNumSlots).References HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getLock(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getUnchecked(), h, Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::set(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::size().Referenced by HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::~HashMap().