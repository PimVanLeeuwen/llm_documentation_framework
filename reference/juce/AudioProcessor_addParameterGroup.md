#### addParameterGroup()


 void AudioProcessor::addParameterGroup ( std::unique\_ptr< AudioProcessorParameterGroup > ) 
 

Adds a group of parameters to the AudioProcessor.All the parameter objects contained within the group will be managed and deleted automatically by the AudioProcessor when no longer needed.See alsoaddParameter