#### addCopiesOf()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 
template<class OtherArrayType > 

 void OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::addCopiesOf ( const OtherArrayType & arrayToAddFrom, 
 
 int startIndex = 0, 
 int numElementsToAdd = 1 ) 

Adds copies of the elements in another array to the end of this array.The other array must be either an OwnedArray of a compatible type of object, or an Array containing pointers to the same kind of object. The objects involved must provide a copy constructor, and this will be used to create new copies of each element, and add them to this array.Parameters

 arrayToAddFrom the array from which to copy the elements 
 
 startIndex the first element of the other array to start copying from 
 numElementsToAdd how many elements to add from the other array. If this value is negative or greater than the number of available elements, all available elements will be copied. 



See alsoadd References createCopyIfNotNull(), OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock(), jassert, and jassertfalse.