#### create() [2/2]


template<typename ParamType > 

 static ModalComponentManager::Callback \* ModalCallbackFunction::create ( void(\* functionToCall )(int, ParamType), ParamType parameterValue ) static 
 

This is a utility function to create a ModalComponentManager::Callback that will call a static function with a parameter.The function that you supply must take two parameters the first being an int, which is the result code that was used when the modal component was dismissed, and the second can be a custom type. Note that this custom value will be copied and stored, so it must be a primitive type or a class that provides copybyvalue semantics.E.g.static void myCallbackFunction (int modalResult, double customValue)
{
 if (modalResult == 1)
 doSomethingWith (customValue);
}
 
Component\* someKindOfComp;
...
someKindOfComp>enterModalState (true, ModalCallbackFunction::create (myCallbackFunction, 3.0));
ComponentThe base class for all JUCE userinterface objects.Definition juce\_Component.h:48
Component::enterModalStatevoid enterModalState(bool takeKeyboardFocus=true, ModalComponentManager::Callback \*callback=nullptr, bool deleteWhenDismissed=false)Puts the component into a modal state.
ModalCallbackFunction::createstatic ModalComponentManager::Callback \* create(CallbackFn &&fn)This is a utility function to create a ModalComponentManager::Callback that will call a callable obje...Definition juce\_ModalComponentManager.h:193
 See alsoModalComponentManager::Callback