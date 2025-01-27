#### setStateInformation()


 virtual void AudioProcessor::setStateInformation ( const void \* data, int sizeInBytes ) pure virtual 
 

This must restore the processor's state from a block of data previously created using getStateInformation().Note that there's also a setCurrentProgramStateInformation() method, which tries to restore just the current program, not the state of the entire processor.See also the helper function getXmlFromBinary() for loading settings as XML.VST3ClientExtensions::getCompatibleParameterIds() will always be called after setStateInformation() therefore you can use information from the plugin state to determine which parameter mapping to use if necessary.See alsosetCurrentProgramStateInformation, VST3ClientExtensions::getCompatibleParameterIds Implemented in AudioProcessorGraph::AudioGraphIOProcessor, and AudioProcessorGraph.Referenced by StandalonePluginHolder::askUserToLoadState(), and StandalonePluginHolder::reloadPluginState().