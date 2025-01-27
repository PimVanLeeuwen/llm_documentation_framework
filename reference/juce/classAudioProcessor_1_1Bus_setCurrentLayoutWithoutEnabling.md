#### setCurrentLayoutWithoutEnabling()


 bool AudioProcessor::Bus::setCurrentLayoutWithoutEnabling ( const AudioChannelSet & layout ) 
 

Sets the bus's current layout without changing the enabled state.If the AudioProcessor does not support this layout then this will return false.See alsoAudioChannelSet