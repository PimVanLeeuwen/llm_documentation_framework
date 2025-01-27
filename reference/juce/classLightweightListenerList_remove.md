#### remove()


template<typename ListenerClass > 

 void LightweightListenerList< ListenerClass >::remove ( ListenerClass \* listenerToRemove ) 
 

Removes a listener from the list.If the listener wasn't in the list, this has no effect.If you need to remove a Listener during a callback, use the ListenerList type.References jassert.Referenced by LightweightListenerList< ListenerClass >::addScoped().