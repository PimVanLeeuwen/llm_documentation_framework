#### remapTable()


template<typename KeyType , typename ValueType , class HashFunctionType = DefaultHashFunctions, class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::remapTable ( int newNumberOfSlots ) 
 

Remaps the hashmap to use a different number of slots for its hash function.Each slot corresponds to a single hashcode, and each one can contain multiple items.See alsogetNumSlots() References HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getLock(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getNumSlots(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getUnchecked(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::insertMultiple(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::set(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::swapWith().Referenced by HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getReference().