#### operator!=()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 
template<class OtherArrayType > 

 bool Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::operator!= ( const OtherArrayType & other ) const 
 

Compares this array to another one.Two arrays are considered equal if they both contain the same set of elements, in the same order.Parameters

 other the other array to compare with 
 


References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::operator==().