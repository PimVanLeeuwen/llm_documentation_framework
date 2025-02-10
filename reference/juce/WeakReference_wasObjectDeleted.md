#### wasObjectDeleted()


template<class ObjectType , class ReferenceCountingType = ReferenceCountedObject> 

 bool WeakReference< ObjectType, ReferenceCountingType >::wasObjectDeleted ( ) const noexcept 
 

This returns true if this reference has been pointing at an object, but that object has since been deleted.If this reference was only ever pointing at a null pointer, this will return false. Using operator=() to make this refer to a different object will reset this flag to match the status of the reference from which you're copying.References ReferenceCountedObjectPtr< ObjectType >::get().