#### forComponent() [2/2]


template<class ComponentType , typename ParamType > 

 static ModalComponentManager::Callback \* ModalCallbackFunction::forComponent ( void(\* functionToCall )(int, ComponentType \*, ParamType), ComponentType \* component, ParamType param ) static 
 

Creates a ModalComponentManager::Callback that will call a static function with a component.The function that you supply must take three parameters the first being an int, which is the result code that was used when the modal component was dismissed, the second being a Component class, and the third being a custom type (which must be a primitive type or have copybyvalue semantics). The component will be stored as a WeakReference, so that if it gets deleted before this callback is invoked, the pointer that is passed into the function will be null.E.g.static void myCallbackFunction (int modalResult, Slider\* mySlider, String customParam)
{
 if (modalResult == 1 && mySlider != nullptr) // (must check that mySlider isn't null in case it was deleted..)
 mySlider>setName (customParam);
}
 
Component\* someKindOfComp;
Slider\* mySlider;
...
someKindOfComp>enterModalState (true, ModalCallbackFunction::forComponent (myCallbackFunction, mySlider, String ("hello")));
Component::setNamevirtual void setName(const String &newName)Sets the name of this component.
 See alsoModalComponentManager::Callback