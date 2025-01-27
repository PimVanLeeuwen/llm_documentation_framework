#### loadImpulseResponse() [3/3]


 void dsp::Convolution::loadImpulseResponse ( AudioBuffer< float > && buffer, 
 
 double bufferSampleRate, 
 Stereo isStereo, 
 Trim requiresTrimming, 
 Normalise requiresNormalisation ) 

This function loads an impulse response from an audio buffer.To avoid memory allocation on the audio thread, this function takes ownership of the buffer passed in.If calling this function during processing, make sure that the buffer is not allocated on the audio thread (be careful of accidental copies!). If you need to pass arbitrary/generated buffers it's recommended to create these buffers on a separate thread and to use some waitfree construct (a lockfree queue or a SpinLock/GenericScopedTryLock combination) to transfer ownership to the audio thread without allocating.Parameters

 buffer the AudioBuffer to use 
 
 bufferSampleRate the sampleRate of the data in the AudioBuffer 
 isStereo selects either stereo or mono 
 requiresTrimming optionally trim the start and the end of the impulse response 
 requiresNormalisation optionally normalise the impulse response amplitude