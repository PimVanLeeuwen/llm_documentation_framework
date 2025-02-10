#### pushBuffer() [3/3]


 void AudioVisualiserComponent::pushBuffer ( const float \*const \* channelData, 
 
 int numChannels, 
 int numSamples ) 

Pushes a buffer of channels data.The number of channels provided here is expected to match the number of channels that this AudioVisualiserComponent has been told to use.