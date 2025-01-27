#### callCheckedExcluding() [2/2]


template<typename ListenerClass , typename ArrayType = Array<ListenerClass\*>> 
template<typename BailOutCheckerType , typename... MethodArgs, typename... Args> 

 void ListenerList< ListenerClass, ArrayType >::callCheckedExcluding ( ListenerClass \* listenerToExclude, 
 
 const BailOutCheckerType & bailOutChecker, 
 void(ListenerClass::\* callbackFunction )(MethodArgs...), 
 Args &&... args ) 

Calls a specific listener method for each listener in the list, except for the listener specified by listenerToExclude, additionally checking the bailout checker before each call.See the class description for info about writing a bailout checker.References ListenerList< ListenerClass, ArrayType >::callCheckedExcluding().