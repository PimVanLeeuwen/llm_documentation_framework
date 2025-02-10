#### endChangeGesture()


 void AudioProcessorParameter::endChangeGesture ( ) 
 

Tells the host that the user has finished changing this parameter.This allows the host to know when a parameter is actively being held by the user, and it may use this information to help it record automation. A call to this method must follow a call to beginChangeGesture().