#### swapWith()


template<typename KeyType , typename ValueType , class HashFunctionType = DefaultHashFunctions, class TypeOfCriticalSectionToUse = DummyCriticalSection> 
template<class OtherHashMapType > 

 void HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::swapWith ( OtherHashMapType & otherHashMap ) noexcept 
 

Efficiently swaps the contents of two hashmaps.References HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::getLock(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::swapWith().