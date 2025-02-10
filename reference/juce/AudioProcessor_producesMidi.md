#### producesMidi()


 virtual bool AudioProcessor::producesMidi ( ) const pure virtual 
 

Returns true if the processor produces MIDI messages.This must return the same value every time it is called. This may be called by the audio thread, so this should be fast. Ideally, just return a constant.Implemented in AudioProcessorGraph::AudioGraphIOProcessor, and AudioProcessorGraph.