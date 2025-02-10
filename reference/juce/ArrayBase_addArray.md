#### addArray() [4/4]


template<class ElementType , class TypeOfCriticalSectionToUse > 
template<class OtherArrayType > 

 std::enable\_if\_t<! std::is\_pointer\_v< OtherArrayType >, int > ArrayBase< ElementType, TypeOfCriticalSectionToUse >::addArray ( const OtherArrayType & arrayToAddFrom, 
 
 int startIndex, 
 int numElementsToAdd = 1 ) 

References ArrayBase< ElementType, TypeOfCriticalSectionToUse >::addArray(), jassert, and jassertfalse.