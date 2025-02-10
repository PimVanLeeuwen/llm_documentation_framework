#### callChecked() [2/2]


template<typename ListenerClass > 
template<typename BailOutCheckerType , typename... MethodArgs, typename... Args> 

 void LightweightListenerList< ListenerClass >::callChecked ( const BailOutCheckerType & bailOutChecker, 
 
 void(ListenerClass::\* callbackFunction )(MethodArgs...), 
 Args &&... args ) const 

Calls a specific listener method for each listener in the list, additionally checking the bailout checker before each call.See the class description for info about writing a bailout checker.References LightweightListenerList< ListenerClass >::callCheckedExcluding().