#### setInputChannelMapping()


 void ChannelRemappingAudioSource::setInputChannelMapping ( int destChannelIndex, 
 
 int sourceChannelIndex ) 

Creates an input channel mapping.When the getNextAudioBlock() method is called, the data in channel sourceChannelIndex of the incoming data will be sent to destChannelIndex of our input source.Parameters

 destChannelIndex the index of an input channel in our input audio source (i.e. the source specified when this object was created). 
 
 sourceChannelIndex the index of the input channel in the incoming audio data buffer during our getNextAudioBlock() callback