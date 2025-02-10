#### remove()


template<typename KeyType , typename ValueType , class HashFunctionType = DefaultHashFunctions, class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::remove ( KeyTypeParameter keyToRemove ) 
 

Removes an item with the given key.References HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getLock(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getNumSlots(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getUnchecked(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::set().