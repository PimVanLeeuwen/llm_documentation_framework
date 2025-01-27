#### operator=()


template<class ObjectType > 

 OptionalScopedPointer & OptionalScopedPointer< ObjectType >::operator= ( OptionalScopedPointer< ObjectType > && other ) noexcept 
 

Takes ownership of the object that another OptionalScopedPointer holds.Like a normal std::unique\_ptr, the objectToTransferFrom object will become null, as ownership of the managed object is transferred to this object.The ownership flag that says whether or not to delete the managed object is also copied from the source object.References OptionalScopedPointer< ObjectType >::swapWith().