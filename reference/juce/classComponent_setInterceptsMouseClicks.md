#### setInterceptsMouseClicks()


 void Component::setInterceptsMouseClicks ( bool allowClicksOnThisComponent, bool allowClicksOnChildComponents ) noexcept 
 

Changes the default return value for the hitTest() method.Setting this to false is an easy way to make a component pass all its mouse events (not just clicks) through to the components behind it.When a component is created, the default setting for this is true.Parameters

 allowClicksOnThisComponent if true, hitTest() will always return true; if false, it will return false (or true for child components if allowClicksOnChildComponents is true) 
 
 allowClicksOnChildComponents if this is true and allowClicksOnThisComponent is false, then child components can be clicked on as normal but clicks on this component pass straight through; if this is false and allowClicksOnThisComponent is false, then neither this component nor any child components can be clicked on 



See alsohitTest, getInterceptsMouseClicks