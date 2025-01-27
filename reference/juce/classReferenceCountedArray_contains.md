#### contains() [2/2]


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 bool ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::contains ( const ObjectClassPtr & objectToLookFor ) const noexcept 
 

Returns true if the array contains a specified object.Parameters

 objectToLookFor the object to look for 
 



Returnstrue if the object is in the array References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::contains().Referenced by ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::contains().