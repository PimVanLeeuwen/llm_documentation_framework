#### addRange()


template<class Type > 

 void SparseSet< Type >::addRange ( Range< Type > range ) 
 

Adds a range of contiguous values to the set.e.g. addRange (Range <int> (10, 14)) will add (10, 11, 12, 13) to the set.References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::add(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::begin(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::end(), Range< ValueType >::isEmpty(), and SparseSet< Type >::removeRange().Referenced by SparseSet< Type >::invertRange().