#### acceptsMidi()


 bool AudioProcessorGraph::acceptsMidi ( ) const overridevirtual 
 

Returns true if the processor wants MIDI messages.This must return the same value every time it is called. This may be called by the audio thread, so this should be fast. Ideally, just return a constant.Implements AudioProcessor.