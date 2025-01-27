#### clear()


template<class ObjectType , class ReferenceCountingType = ReferenceCountedObject> 

 void WeakReference< ObjectType, ReferenceCountingType >::Master::clear ( ) noexcept 
 

The object that owns this master pointer should call this before it gets destroyed, to zero all the references to this object that may be out there.See the WeakReference class notes for an example of how to do this.