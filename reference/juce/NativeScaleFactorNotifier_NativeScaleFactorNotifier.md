#### NativeScaleFactorNotifier()


 NativeScaleFactorNotifier::NativeScaleFactorNotifier ( Component \* comp, 
 
 std::function< void(float)> onScaleChanged ) 

Constructs an instance.While the instance is alive, it will listen for changes to the scale factor of the comp's peer, and will call onScaleChanged whenever this scale factor changes.Parameters

 comp The component to observe 
 
 onScaleChanged A function that will be called when the backing scale factor changes