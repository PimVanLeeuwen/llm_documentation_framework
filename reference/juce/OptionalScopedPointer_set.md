#### set()


template<class ObjectType > 

 void OptionalScopedPointer< ObjectType >::set ( ObjectType \* newObject, 
 
 bool takeOwnership ) 

Makes this OptionalScopedPointer point at a new object, specifying whether the OptionalScopedPointer will take ownership of the object.If takeOwnership is true, then the OptionalScopedPointer will act like a std::unique\_ptr, deleting the object when it is itself deleted. If this parameter is false, then the OptionalScopedPointer just holds a normal pointer to the object, and won't delete it.References OptionalScopedPointer< ObjectType >::get(), and OptionalScopedPointer< ObjectType >::reset().Referenced by OptionalScopedPointer< ObjectType >::setNonOwned(), and OptionalScopedPointer< ObjectType >::setOwned().