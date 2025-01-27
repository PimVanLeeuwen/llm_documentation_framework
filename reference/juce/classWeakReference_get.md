#### get()


template<class ObjectType , class ReferenceCountingType = ReferenceCountedObject> 

 ObjectType \* WeakReference< ObjectType, ReferenceCountingType >::get ( ) const noexcept 
 

Returns the object that this pointer refers to, or null if the object no longer exists.References ReferenceCountedObjectPtr< ObjectType >::get().Referenced by WeakReference< Component >::operator Component \*(), and WeakReference< ObjectType, ReferenceCountingType >::operator>().