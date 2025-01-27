#### withParam()


template<typename ParamType1 , typename ParamType2 > 

 static ModalComponentManager::Callback \* ModalCallbackFunction::withParam ( void(\* functionToCall )(int, ParamType1, ParamType2), ParamType1 parameterValue1, ParamType2 parameterValue2 ) static 
 

This is a utility function to create a ModalComponentManager::Callback that will call a static function with two custom parameters.The function that you supply must take three parameters the first being an int, which is the result code that was used when the modal component was dismissed, and the next two are your custom types. Note that these custom values will be copied and stored, so they must be primitive types or classes that provide copybyvalue semantics.E.g.static void myCallbackFunction (int modalResult, double customValue1, String customValue2)
{
 if (modalResult == 1)
 doSomethingWith (customValue1, customValue2);
}
 
Component\* someKindOfComp;
...
someKindOfComp>enterModalState (true, ModalCallbackFunction::create (myCallbackFunction, 3.0, String ("xyz")));
StringThe JUCE String class!Definition juce\_String.h:68
 See alsoModalComponentManager::Callback