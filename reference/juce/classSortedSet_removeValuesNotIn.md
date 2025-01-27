#### removeValuesNotIn()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 
template<class OtherSetType > 

 void SortedSet< ElementType, TypeOfCriticalSectionToUse >::removeValuesNotIn ( const OtherSetType & otherSet ) noexcept 
 

Removes any elements which are not found in another set.Only elements which occur in this other set will be retained.Parameters

 otherSet the set in which to look for elements NOT to remove 
 



See alsoremoveValuesIn, remove, removeValue, removeRange