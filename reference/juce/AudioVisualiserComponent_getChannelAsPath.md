#### getChannelAsPath()


 void AudioVisualiserComponent::getChannelAsPath ( Path & result, 
 
 const Range< float > \* levels, 
 int numLevels, 
 int nextSample ) 

Creates a path which contains the waveform shape of a given set of range data.The path is normalised so that 1 and +1 are its upper and lower bounds, and it goes from 0 to numLevels on the X axis.