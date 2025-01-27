#### removeRange()


template<class Type > 

 void SparseSet< Type >::removeRange ( Range< Type > rangeToRemove ) 
 

Removes a range of values from the set.e.g. removeRange (Range<int> (10, 14)) will remove (10, 11, 12, 13) from the set.References Range< ValueType >::contains(), Range< ValueType >::getEnd(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getReference(), Range< ValueType >::getStart(), SparseSet< Type >::getTotalRange(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::insert(), Range< ValueType >::isEmpty(), jassert, Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::remove(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::size().Referenced by SparseSet< Type >::addRange(), and SparseSet< Type >::invertRange().