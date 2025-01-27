#### getNumSlots()


template<typename KeyType , typename ValueType , class HashFunctionType = DefaultHashFunctions, class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 int HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getNumSlots ( ) const noexcept 
 

Returns the number of slots which are available for hashing.Each slot corresponds to a single hashcode, and each one can contain multiple items.See alsogetNumSlots() References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::size().Referenced by HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::containsValue(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getReference(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::Iterator::next(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::remapTable(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::remove(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::removeValue(), and HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::Iterator::resetToEnd().