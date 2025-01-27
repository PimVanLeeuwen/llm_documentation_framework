#### add()


template<typename ListenerClass , typename ArrayType = Array<ListenerClass\*>> 

 void ListenerList< ListenerClass, ArrayType >::add ( ListenerClass \* listenerToAdd ) 
 

Adds a listener to the list.A listener can only be added once, so if the listener is already in the list, this method has no effect.If a Listener is added during a callback, it is guaranteed not to be called in the same iteration.See alsoremove References jassertfalse.Referenced by ListenerList< ListenerClass, ArrayType >::addScoped().