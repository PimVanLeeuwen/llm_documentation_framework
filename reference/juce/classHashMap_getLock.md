#### getLock()


template<typename KeyType , typename ValueType , class HashFunctionType = DefaultHashFunctions, class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 const TypeOfCriticalSectionToUse & HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getLock ( ) const noexcept 
 

Returns the CriticalSection that locks this structure.To lock, you can call getLock().enter() and getLock().exit(), or preferably use an object of ScopedLockType as an RAII lock for it.Referenced by HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::clear(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::contains(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::containsValue(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getReference(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::operator[](), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::remapTable(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::remove(), HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::removeValue(), and HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::swapWith().