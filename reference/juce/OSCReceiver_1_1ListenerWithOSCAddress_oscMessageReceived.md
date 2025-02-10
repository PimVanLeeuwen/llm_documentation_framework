#### oscMessageReceived()


template<typename CallbackType = MessageLoopCallback> 

 virtual void OSCReceiver::ListenerWithOSCAddress< CallbackType >::oscMessageReceived ( const OSCMessage & message ) pure virtual 
 

Called when the OSCReceiver receives an OSC message with an OSC address pattern that matches the OSC address with which this listener was added.