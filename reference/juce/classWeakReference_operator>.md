#### operator>()


template<class ObjectType , class ReferenceCountingType = ReferenceCountedObject> 

 ObjectType \* WeakReference< ObjectType, ReferenceCountingType >::operator> ( ) const noexcept 
 

Returns the object that this pointer refers to, or null if the object no longer exists.References WeakReference< ObjectType, ReferenceCountingType >::get().