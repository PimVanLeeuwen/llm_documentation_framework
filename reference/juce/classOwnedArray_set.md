#### set() [2/2]


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClass \* OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::set ( int indexToChange, 
 
 std::unique\_ptr< ObjectClass > newObject, 
 bool deleteOldElement = true ) 

Replaces an object in the array with a different one.If the index is less than zero, this method does nothing. If the index is beyond the end of the array, the new object is added to the end of the array.Be careful not to add the same object to the array more than once, as this will obviously cause deletion of dangling pointers.Parameters

 indexToChange the index whose value you want to change 
 
 newObject the new value to set for this index. 
 deleteOldElement whether to delete the object that's being replaced with the new one 



See alsoadd, insert, remove References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::set().