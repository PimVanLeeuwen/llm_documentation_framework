#### clear()


template<typename ListenerClass , typename ArrayType = Array<ListenerClass\*>> 

 void ListenerList< ListenerClass, ArrayType >::clear ( ) 
 

Clears the list.If the ListenerList is cleared during a callback, it is guaranteed that no more listeners will be called.Referenced by ListenerList< ListenerClass, ArrayType >::~ListenerList().