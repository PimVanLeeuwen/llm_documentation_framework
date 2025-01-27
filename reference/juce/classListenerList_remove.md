#### remove()


template<typename ListenerClass , typename ArrayType = Array<ListenerClass\*>> 

 void ListenerList< ListenerClass, ArrayType >::remove ( ListenerClass \* listenerToRemove ) 
 

Removes a listener from the list.If the listener wasn't in the list, this has no effect.If a Listener is removed during a callback, it is guaranteed not to be called if it hasn't already been called.References end(), and jassert.Referenced by ListenerList< ListenerClass, ArrayType >::addScoped().