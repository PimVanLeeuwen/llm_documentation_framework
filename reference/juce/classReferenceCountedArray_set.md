#### set() [2/2]


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::set ( int indexToChange, 
 
 const ObjectClassPtr & newObject ) 

Replaces an object in the array with a different one.If the index is less than zero, this method does nothing. If the index is beyond the end of the array, the new object is added to the end of the array.The object being added has its reference count increased, and if it's replacing another object, then that one has its reference count decreased, and may be deleted.Parameters

 indexToChange the index whose value you want to change 
 
 newObject the new value to set for this index. 



See alsoadd, insert, remove References ReferenceCountedObjectPtr< ObjectType >::get(), and ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::set().Referenced by ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::set().