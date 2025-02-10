#### getLastEnabledLayout()


 const AudioChannelSet & AudioProcessor::Bus::getLastEnabledLayout ( ) const noexcept 
 

Return the bus's last active channel layout.If the bus is currently enabled then the result will be identical to getCurrentLayout otherwise it will return the last enabled layout.See alsoAudioChannelSet