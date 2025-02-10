#### callChecked() [2/2]


template<typename ListenerClass , typename ArrayType = Array<ListenerClass\*>> 
template<typename BailOutCheckerType , typename... MethodArgs, typename... Args> 

 void ListenerList< ListenerClass, ArrayType >::callChecked ( const BailOutCheckerType & bailOutChecker, 
 
 void(ListenerClass::\* callbackFunction )(MethodArgs...), 
 Args &&... args ) 

Calls a specific listener method for each listener in the list, additionally checking the bailout checker before each call.See the class description for info about writing a bailout checker.References ListenerList< ListenerClass, ArrayType >::callCheckedExcluding().