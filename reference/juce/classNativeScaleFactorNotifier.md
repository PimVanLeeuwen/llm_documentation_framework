Calls a function every time the native scale factor of a component's peer changes.This is used in the VST and VST3 wrappers to ensure that the editor's scale is kept in sync with the scale of its containing component.

Constructor & Destructor Documentation


◆ NativeScaleFactorNotifier()


 NativeScaleFactorNotifier::NativeScaleFactorNotifier ( Component \* comp, 
 
 std::function< void(float)> onScaleChanged ) 

Constructs an instance.While the instance is alive, it will listen for changes to the scale factor of the comp's peer, and will call onScaleChanged whenever this scale factor changes.Parameters

 comp The component to observe 
 
 onScaleChanged A function that will be called when the backing scale factor changes 





◆ ~NativeScaleFactorNotifier()


 NativeScaleFactorNotifier::~NativeScaleFactorNotifier ( ) override 
 