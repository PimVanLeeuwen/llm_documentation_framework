#### get()


template<class ElementType , bool throwOnFailure = false> 

 ElementType \* HeapBlock< ElementType, throwOnFailure >::get ( ) const noexcept 
 

Returns a raw pointer to the allocated data.This may be a null pointer if the data hasn't yet been allocated, or if it has been freed by calling the free() method.Referenced by SpeakerMappings::VstSpeakerConfigurationHolder::get(), and AudioBuffer< Type >::setSize().