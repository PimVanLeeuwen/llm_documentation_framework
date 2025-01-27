#### isMidiEffect()


 virtual bool AudioProcessor::isMidiEffect ( ) const virtual 
 

Returns true if this is a MIDI effect plugin and does no audio processing.This must return the same value every time it is called. This may be called by the audio thread, so this should be fast. Ideally, just return a constant.Referenced by StandalonePluginHolder::reloadAudioDeviceState().