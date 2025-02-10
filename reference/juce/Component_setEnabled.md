#### setEnabled()


 void Component::setEnabled ( bool shouldBeEnabled ) 
 

Enables or disables this component.Disabling a component will also cause all of its child components to become disabled.Similarly, enabling a component which is inside a disabled parent component won't make any difference until the parent is reenabled.See alsoisEnabled, enablementChanged