#### decReferenceCountWithoutDeleting()


 bool SingleThreadedReferenceCountedObject::decReferenceCountWithoutDeleting ( ) noexcept 
 

Decreases the object's reference count.If the count gets to zero, the object will not be deleted, but this method will return true, allowing the caller to take care of deletion.References jassert.