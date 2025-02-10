#### setSize()


template<typename Type > 

 void AudioBuffer< Type >::setSize ( int newNumChannels, 
 
 int newNumSamples, 
 bool keepExistingContent = false, 
 bool clearExtraSpace = false, 
 bool avoidReallocating = false ) 

Changes the buffer's size or number of channels.This can expand or contract the buffer's length, and add or remove channels.Note that if keepExistingContent and avoidReallocating are both true, then it will only avoid reallocating if neither the channel count or length in samples increase.If the required memory can't be allocated, this will throw a std::bad\_alloc exception.Parameters

 newNumChannels the new number of channels. 
 
 newNumSamples the new number of samples. 
 keepExistingContent if this is true, it will try to preserve as much of the old data as it can in the new buffer. 
 clearExtraSpace if this is true, then any extra channels or space that is allocated will be also be cleared. If false, then this space is left uninitialised. 
 avoidReallocating if this is true, then changing the buffer's size won't reduce the amount of memory that is currently allocated (but it will still increase it if the new size is bigger than the amount it currently has). If this is false, then a new allocation will be done so that the buffer uses takes up the minimum amount of memory that it needs. 


References HeapBlock< ElementType, throwOnFailure >::allocate(), HeapBlock< ElementType, throwOnFailure >::clear(), HeapBlock< ElementType, throwOnFailure >::get(), jassert, jmin(), HeapBlock< ElementType, throwOnFailure >::swapWith(), and unalignedPointerCast().Referenced by AudioBuffer< Type >::makeCopyOf(), and AudioBuffer< Type >::operator=().