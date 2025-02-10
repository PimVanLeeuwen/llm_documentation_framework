#### operator!=()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 bool SortedSet< ElementType, TypeOfCriticalSectionToUse >::operator!= ( const SortedSet< ElementType > & other ) const noexcept 
 

Compares this set to another one.Two sets are considered equal if they both contain the same set of elements.Parameters

 other the other set to compare with 
 


References operator==().