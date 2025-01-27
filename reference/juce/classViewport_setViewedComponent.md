#### setViewedComponent()


 void Viewport::setViewedComponent ( Component \* newViewedComponent, 
 
 bool deleteComponentWhenNoLongerNeeded = true ) 

Sets the component that this viewport will contain and scroll around.This will add the given component to this Viewport and position it at (0, 0).(Don't add or remove any child components directly using the normal Component::addChildComponent() methods).Parameters

 newViewedComponent the component to add to this viewport, or null to remove the current component. 
 
 deleteComponentWhenNoLongerNeeded if true, the component will be deleted automatically when the viewport is deleted or when a different component is added. If false, the caller must manage the lifetime of the component 



See alsogetViewedComponent