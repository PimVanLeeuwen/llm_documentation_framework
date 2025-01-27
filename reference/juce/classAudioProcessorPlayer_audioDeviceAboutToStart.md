#### audioDeviceAboutToStart()


 void AudioProcessorPlayer::audioDeviceAboutToStart ( AudioIODevice \* device ) overridevirtual 
 

Called to indicate that the device is about to start calling back.This will be called just before the audio callbacks begin, either when this callback has just been added to an audio device, or after the device has been restarted because of a samplerate or blocksize change.You can use this opportunity to find out the sample rate and block size that the device is going to use by calling the AudioIODevice::getCurrentSampleRate() and AudioIODevice::getCurrentBufferSizeSamples() on the supplied pointer.Parameters

 device the audio IO device that will be used to drive the callback. Note that if you're going to store this this pointer, it is only valid until the next time that audioDeviceStopped is called. 
 


Implements AudioIODeviceCallback.