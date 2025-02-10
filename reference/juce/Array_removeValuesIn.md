#### removeValuesIn()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 
template<class OtherArrayType > 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::removeValuesIn ( const OtherArrayType & otherArray ) 
 

Removes any elements which are also in another array.Parameters

 otherArray the other array in which to look for elements to remove 
 



See alsoremoveValuesNotIn, remove, removeFirstMatchingValue, removeAllInstancesOf, removeRange References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::clear(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().Referenced by LassoComponent< SelectableItemType >::dragLasso().