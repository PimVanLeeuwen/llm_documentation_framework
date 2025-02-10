#### isLayoutSupported()


 bool AudioProcessor::Bus::isLayoutSupported ( const AudioChannelSet & set, 
 
 BusesLayout \* currentLayout = nullptr ) const 

Checks if a particular layout is supported.Parameters

 set The AudioChannelSet which is to be probed. 
 
 currentLayout If nonnull, pretend that the current layout of the AudioProcessor is currentLayout. On exit, currentLayout will be modified to represent the buses layouts of the AudioProcessor as if the layout of the receiver had been successfully changed. This is useful as changing the layout of the receiver may change the bus layout of other buses. 



See alsoAudioChannelSet