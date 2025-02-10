#### callExcluding() [2/2]


template<typename ListenerClass > 
template<typename... MethodArgs, typename... Args> 

 void LightweightListenerList< ListenerClass >::callExcluding ( ListenerClass \* listenerToExclude, 
 
 void(ListenerClass::\* callbackFunction )(MethodArgs...), 
 Args &&... args ) const 

Calls a specific listener method for each listener in the list, except for the listener specified by listenerToExclude.References LightweightListenerList< ListenerClass >::callCheckedExcluding().