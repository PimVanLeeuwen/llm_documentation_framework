#### readSamples()


 virtual bool AudioFormatReader::readSamples ( int \*const \* destChannels, int numDestChannels, int startOffsetInDestBuffer, int64 startSampleInFile, int numSamples ) pure virtual 
 

Subclasses must implement this method to perform the lowlevel read operation.Callers should use read() instead of calling this directly.Parameters

 destChannels the array of destination buffers to fill. Some of these pointers may be null 
 
 numDestChannels the number of items in the destChannels array. This value is guaranteed not to be greater than the number of channels that this reader object contains 
 startOffsetInDestBuffer the number of samples from the start of the dest data at which to begin writing 
 startSampleInFile the number of samples into the source data at which to begin reading. This value is guaranteed to be >= 0. 
 numSamples the number of samples to read 


Implemented in ARAAudioSourceReader, ARAPlaybackRegionReader, AudioCDReader, AudioSubsectionReader, and BufferingAudioReader.