#### callExcluding() [2/2]


template<typename ListenerClass , typename ArrayType = Array<ListenerClass\*>> 
template<typename... MethodArgs, typename... Args> 

 void ListenerList< ListenerClass, ArrayType >::callExcluding ( ListenerClass \* listenerToExclude, 
 
 void(ListenerClass::\* callbackFunction )(MethodArgs...), 
 Args &&... args ) 

Calls a specific listener method for each listener in the list, except for the listener specified by listenerToExclude.References ListenerList< ListenerClass, ArrayType >::callCheckedExcluding().