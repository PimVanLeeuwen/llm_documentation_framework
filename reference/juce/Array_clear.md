#### clear()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::clear ( ) 
 

Removes all elements from the array.This will remove all the elements, and free any storage that the array is using. To clear the array without freeing the storage, use the clearQuick() method instead.See alsoclearQuick References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::clearQuick(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().Referenced by SparseSet< Type >::clear(), LassoComponent< SelectableItemType >::endLasso(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::removeValuesIn(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::removeValuesNotIn().