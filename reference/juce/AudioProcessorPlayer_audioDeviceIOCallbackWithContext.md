#### audioDeviceIOCallbackWithContext()


 void AudioProcessorPlayer::audioDeviceIOCallbackWithContext ( const float \*const \* inputChannelData, int numInputChannels, float \*const \* outputChannelData, int numOutputChannels, int numSamples, const AudioIODeviceCallbackContext & context ) overridevirtual 
 

Processes a block of incoming and outgoing audio data.The subclass's implementation should use the incoming audio for whatever purposes it needs to, and must fill all the output channels with the next block of output data before returning.The channel data is arranged with the same array indices as the channel name array returned by AudioIODevice::getOutputChannelNames(), but those channels that aren't specified in AudioIODevice::open() will have a null pointer for their associated channel, so remember to check for this.Parameters

 inputChannelData a set of arrays containing the audio data for each incoming channel this data is valid until the function returns. There will be one channel of data for each input channel that was enabled when the audio device was opened (see AudioIODevice::open()) 
 
 numInputChannels the number of pointers to channel data in the inputChannelData array. 
 outputChannelData a set of arrays which need to be filled with the data that should be sent to each outgoing channel of the device. There will be one channel of data for each output channel that was enabled when the audio device was opened (see AudioIODevice::open()) The initial contents of the array is undefined, so the callback function must fill all the channels with zeros if its output is silence. Failing to do this could cause quite an unpleasant noise! 
 numOutputChannels the number of pointers to channel data in the outputChannelData array. 
 numSamples the number of samples in each channel of the input and output arrays. The number of samples will depend on the audio device's buffer size and will usually remain constant, although this isn't guaranteed. For example, on Android, on devices which support it, Android will chop up your audio processing into several smaller callbacks to ensure higher audio performance. So make sure your code can cope with reasonable changes in the buffer size from one callback to the next. 
 context Additional information that may be passed to the AudioIODeviceCallback. 


Reimplemented from AudioIODeviceCallback.