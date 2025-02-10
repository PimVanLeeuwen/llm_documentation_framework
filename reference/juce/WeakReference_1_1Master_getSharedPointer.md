#### getSharedPointer()


template<class ObjectType , class ReferenceCountingType = ReferenceCountedObject> 

 SharedRef WeakReference< ObjectType, ReferenceCountingType >::Master::getSharedPointer ( ObjectType \* object ) 
 

The first call to this method will create an internal object that is shared by all weak references to the object.References ReferenceCountedObjectPtr< ObjectType >::get(), and jassert.