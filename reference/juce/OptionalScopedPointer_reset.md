#### reset()


template<class ObjectType > 

 void OptionalScopedPointer< ObjectType >::reset ( ) noexcept 
 

Resets this pointer to null, possibly deleting the object that it holds, if it has ownership of it.Referenced by OptionalScopedPointer< ObjectType >::clear(), OptionalScopedPointer< ObjectType >::set(), and OptionalScopedPointer< ObjectType >::~OptionalScopedPointer().