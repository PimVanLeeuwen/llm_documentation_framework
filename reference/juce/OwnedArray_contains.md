#### contains()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 bool OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::contains ( const ObjectClass \* objectToLookFor ) const noexcept 
 

Returns true if the array contains a specified object.Parameters

 objectToLookFor the object to look for 
 



Returnstrue if the object is in the array References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().