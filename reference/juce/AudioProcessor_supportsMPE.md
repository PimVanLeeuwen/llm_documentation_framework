#### supportsMPE()


 virtual bool AudioProcessor::supportsMPE ( ) const virtual 
 

Returns true if the processor supports MPE.This must return the same value every time it is called. This may be called by the audio thread, so this should be fast. Ideally, just return a constant.