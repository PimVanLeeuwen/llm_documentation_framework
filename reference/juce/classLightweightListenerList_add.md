#### add()


template<typename ListenerClass > 

 void LightweightListenerList< ListenerClass >::add ( ListenerClass \* listenerToAdd ) 
 

Adds a listener to the list.A listener can only be added once, so if the listener is already in the list, this method has no effect.If you need to add a Listener during a callback, use the ListenerList type.See alsoremove References jassert, and jassertfalse.Referenced by LightweightListenerList< ListenerClass >::addScoped().