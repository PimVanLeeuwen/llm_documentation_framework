#### isRealtime()


 Realtime AudioProcessor::isRealtime ( ) const noexcept 
 

Returns no if the processor is being run in an offline mode for rendering.If the processor is being run live on realtime signals, this returns yes. If the mode is unknown, this will assume it's realtime and return yes.This value may be unreliable until the prepareToPlay() method has been called, and could change each time prepareToPlay() is called.See alsosetNonRealtime()