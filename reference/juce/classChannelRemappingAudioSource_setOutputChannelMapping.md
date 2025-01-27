#### setOutputChannelMapping()


 void ChannelRemappingAudioSource::setOutputChannelMapping ( int sourceChannelIndex, 
 
 int destChannelIndex ) 

Creates an output channel mapping.When the getNextAudioBlock() method is called, the data returned in channel sourceChannelIndex by our input audio source will be copied to channel destChannelIndex of the final buffer.Parameters

 sourceChannelIndex the index of an output channel coming from our input audio source (i.e. the source specified when this object was created). 
 
 destChannelIndex the index of the output channel in the incoming audio data buffer during our getNextAudioBlock() callback