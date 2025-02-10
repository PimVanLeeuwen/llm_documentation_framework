#### beginChangeGesture()


 void AudioProcessorParameter::beginChangeGesture ( ) 
 

Sends a signal to the host to tell it that the user is about to start changing this parameter.This allows the host to know when a parameter is actively being held by the user, and it may use this information to help it record automation. If you call this, it must be matched by a later call to endChangeGesture().