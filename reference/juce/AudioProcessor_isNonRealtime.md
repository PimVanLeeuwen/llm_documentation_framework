#### isNonRealtime()


 bool AudioProcessor::isNonRealtime ( ) const noexcept 
 

Returns true if the processor is being run in an offline mode for rendering.If the processor is being run live on realtime signals, this returns false. If the mode is unknown, this will assume it's realtime and return false.This value may be unreliable until the prepareToPlay() method has been called, and could change each time prepareToPlay() is called.See alsosetNonRealtime()