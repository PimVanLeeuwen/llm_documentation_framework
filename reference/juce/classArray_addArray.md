#### addArray() [4/4]


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 
template<class OtherArrayType > 

 std::enable\_if\_t<! std::is\_pointer\_v< OtherArrayType >, void > Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::addArray ( const OtherArrayType & arrayToAddFrom, 
 
 int startIndex, 
 int numElementsToAdd = 1 ) 

Adds elements from another array to the end of this array.Parameters

 arrayToAddFrom the array from which to copy the elements 
 
 startIndex the first element of the other array to start copying from 
 numElementsToAdd how many elements to add from the other array. If this value is negative or greater than the number of available elements, all available elements will be copied. 



See alsoadd References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().