#### removeValuesNotIn()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 
template<class OtherArrayType > 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::removeValuesNotIn ( const OtherArrayType & otherArray ) 
 

Removes any elements which are not found in another array.Only elements which occur in this other array will be retained.Parameters

 otherArray the array in which to look for elements NOT to remove 
 



See alsoremoveValuesIn, remove, removeFirstMatchingValue, removeAllInstancesOf, removeRange References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::clear(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().