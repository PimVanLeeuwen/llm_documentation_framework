#### oscBundleReceived()


template<typename CallbackType = MessageLoopCallback> 

 virtual void OSCReceiver::Listener< CallbackType >::oscBundleReceived ( const OSCBundle & ) virtual 
 

Called when the OSCReceiver receives a new OSC bundle.If you are not interested in OSC bundles, just ignore this method. The default implementation provided here will simply do nothing.