#### addSet()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 
template<class OtherSetType > 

 void SortedSet< ElementType, TypeOfCriticalSectionToUse >::addSet ( const OtherSetType & setToAddFrom, int startIndex = 0, int numElementsToAdd = 1 ) noexcept 
 

Adds elements from another set to this one.Parameters

 setToAddFrom the set from which to copy the elements 
 
 startIndex the first element of the other set to start copying from 
 numElementsToAdd how many elements to add from the other set. If this value is negative or greater than the number of available elements, all available elements will be copied. 



See alsoadd References jassert, and jassertfalse.