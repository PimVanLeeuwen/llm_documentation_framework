#### getChannelLayoutOfBus()


 AudioChannelSet AudioProcessor::getChannelLayoutOfBus ( bool isInput, int busIndex ) const noexcept 
 

Provides the channel layout of the bus with a given index and direction.If the index, direction combination is invalid then this will return an AudioChannelSet with no channels.