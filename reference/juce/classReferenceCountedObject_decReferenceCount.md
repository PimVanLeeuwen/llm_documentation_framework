#### decReferenceCount()


 void ReferenceCountedObject::decReferenceCount ( ) noexcept 
 

Decreases the object's reference count.If the count gets to zero, the object will be deleted.References jassert.