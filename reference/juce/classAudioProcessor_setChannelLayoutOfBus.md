#### setChannelLayoutOfBus()


 bool AudioProcessor::setChannelLayoutOfBus ( bool isInput, 
 
 int busIndex, 
 const AudioChannelSet & layout ) 

Set the channel layout of the bus with a given index and direction.If the index, direction combination is invalid or the layout is not supported by the audio processor then this method will return false.