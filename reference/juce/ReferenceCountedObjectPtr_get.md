#### get()


template<class ObjectType > 

 ReferencedType \* ReferenceCountedObjectPtr< ObjectType >::get ( ) const noexcept 
 

Returns the object that this pointer references.The pointer returned may be null, of course.Referenced by ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::add(), ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::addIfNotAlreadyThere(), WeakReference< ObjectType, ReferenceCountingType >::get(), WeakReference< ObjectType, ReferenceCountingType >::Master::getSharedPointer(), ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::insert(), ReferenceCountedObjectPtr< ObjectType >::operator=(), ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeObject(), ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::set(), WeakReference< ObjectType, ReferenceCountingType >::wasObjectDeleted(), and WeakReference< ObjectType, ReferenceCountingType >::Master::~Master().