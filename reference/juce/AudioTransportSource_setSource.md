#### setSource()


 void AudioTransportSource::setSource ( PositionableAudioSource \* newSource, 
 
 int readAheadBufferSize = 0, 
 TimeSliceThread \* readAheadThread = nullptr, 
 double sourceSampleRateToCorrectFor = 0.0, 
 int maxNumChannels = 2 ) 

Sets the reader that is being used as the input source.This will stop playback, reset the position to 0 and change to the new reader.The source passed in will not be deleted by this object, so must be managed by the caller.Parameters

 newSource the new input source to use. This may be a nullptr 
 
 readAheadBufferSize a size of buffer to use for reading ahead. If this is zero, no reading ahead will be done; if it's greater than zero, a BufferingAudioSource will be used to do the readingahead. If you set a nonzero value here, you'll also need to set the readAheadThread parameter. 
 readAheadThread if you set readAheadBufferSize to a nonzero value, then you'll also need to supply this TimeSliceThread object for the background reader to use. The thread object must not be deleted while the AudioTransport source is still using it. 
 sourceSampleRateToCorrectFor if this is nonzero, it specifies the sample rate of the source, and playback will be samplerate adjusted to maintain playback at the correct pitch. If this is 0, no samplerate adjustment will be performed 
 maxNumChannels the maximum number of channels that may need to be played