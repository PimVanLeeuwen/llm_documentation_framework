#### getStateInformation()


 void AudioProcessorGraph::getStateInformation ( juce::MemoryBlock & destData ) overridevirtual 
 

The host will call this method when it wants to save the processor's internal state.This must copy any info about the processor's state into the block of memory provided, so that the host can store this and later restore it using setStateInformation().Note that there's also a getCurrentProgramStateInformation() method, which only stores the current program, not the state of the entire processor.See also the helper function copyXmlToBinary() for storing settings as XML.See alsogetCurrentProgramStateInformation Implements AudioProcessor.