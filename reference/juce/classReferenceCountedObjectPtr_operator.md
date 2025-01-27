#### operator ReferencedType \*()


template<class ObjectType > 

 ReferenceCountedObjectPtr< ObjectType >::operator ReferencedType \* ( ) const noexcept 
 

Returns the object that this pointer references.The pointer returned may be null, of course. Note that this methods allows the compiler to be very lenient with what it allows you to do with the pointer, it's safer to disable this by setting JUCE\_STRICT\_REFCOUNTEDPOINTER=1, which increased type safety and can prevent some common slipups.