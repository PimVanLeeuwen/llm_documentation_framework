#### oscMessageReceived()


template<typename CallbackType = MessageLoopCallback> 

 virtual void OSCReceiver::Listener< CallbackType >::oscMessageReceived ( const OSCMessage & message ) pure virtual 
 

Called when the OSCReceiver receives a new OSC message.You must implement this function.