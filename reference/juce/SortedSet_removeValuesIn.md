#### removeValuesIn()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 
template<class OtherSetType > 

 void SortedSet< ElementType, TypeOfCriticalSectionToUse >::removeValuesIn ( const OtherSetType & otherSet ) noexcept 
 

Removes any elements which are also in another set.Parameters

 otherSet the other set in which to look for elements to remove 
 



See alsoremoveValuesNotIn, remove, removeValue, removeRange