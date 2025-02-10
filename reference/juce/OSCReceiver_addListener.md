#### addListener() [4/4]


 void OSCReceiver::addListener ( ListenerWithOSCAddress< RealtimeCallback > \* listenerToAdd, 
 
 OSCAddress addressToMatch ) 

Adds a filtered listener that listens to OSC messages matching the address used to register the listener here.The listener will be called on the application's message loop.