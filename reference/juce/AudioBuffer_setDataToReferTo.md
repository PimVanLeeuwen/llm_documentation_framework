#### setDataToReferTo() [2/2]


template<typename Type > 

 void AudioBuffer< Type >::setDataToReferTo ( Type \*const \* dataToReferTo, 
 
 int newNumChannels, 
 int newNumSamples ) 

Makes this buffer point to a preallocated set of channel data arrays.There's also a constructor that lets you specify arrays like this, but this lets you change the channels dynamically.Note that if the buffer is resized or its number of channels is changed, it will reallocate memory internally and copy the existing data to this new area, so it will then stop directly addressing this memory.The hasBeenCleared method will return false after this call.Parameters

 dataToReferTo a preallocated array containing pointers to the data for each channel that should be used by this buffer. The buffer will only refer to this memory, it won't try to delete it when the buffer is deleted or resized. 
 
 newNumChannels the number of channels to use this must correspond to the number of elements in the array passed in 
 newNumSamples the number of samples to use this must correspond to the size of the arrays passed in 


References AudioBuffer< Type >::setDataToReferTo().