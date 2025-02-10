#### acceptsMidi()


 virtual bool AudioProcessor::acceptsMidi ( ) const pure virtual 
 

Returns true if the processor wants MIDI messages.This must return the same value every time it is called. This may be called by the audio thread, so this should be fast. Ideally, just return a constant.Implemented in AudioProcessorGraph, and AudioProcessorGraph::AudioGraphIOProcessor.