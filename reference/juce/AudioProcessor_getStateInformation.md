#### getStateInformation()


 virtual void AudioProcessor::getStateInformation ( juce::MemoryBlock & destData ) pure virtual 
 

The host will call this method when it wants to save the processor's internal state.This must copy any info about the processor's state into the block of memory provided, so that the host can store this and later restore it using setStateInformation().Note that there's also a getCurrentProgramStateInformation() method, which only stores the current program, not the state of the entire processor.See also the helper function copyXmlToBinary() for storing settings as XML.See alsogetCurrentProgramStateInformation Implemented in AudioProcessorGraph::AudioGraphIOProcessor, and AudioProcessorGraph.Referenced by StandalonePluginHolder::askUserToSaveState(), and StandalonePluginHolder::savePluginState().