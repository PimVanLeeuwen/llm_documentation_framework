#### getValue()


template<typename KeyType , typename ValueType , class HashFunctionType = DefaultHashFunctions, class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ValueType HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::Iterator::getValue ( ) const 
 

Returns the current item's value.This should only be called when a call to next() has just returned true.Referenced by HashMap< KeyType, ValueType, HashFunctionType, TypeOfCriticalSectionToUse >::Iterator::operator\*().