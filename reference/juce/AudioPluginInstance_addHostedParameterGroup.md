#### addHostedParameterGroup()


 void AudioPluginInstance::addHostedParameterGroup ( std::unique\_ptr< AudioProcessorParameterGroup > ) 
 

Adds multiple parameters to this instance.In debug mode, this will also check that all added parameters derive from HostedParameter.See alsoAudioProcessor::addParameterGroup()