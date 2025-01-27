#### setContent()


 void SidePanel::setContent ( Component \* newContentComponent, 
 
 bool deleteComponentWhenNoLongerNeeded = true ) 

Sets the component that this SidePanel will contain.This will add the given component to this SidePanel and position it below the title bar.(Don't add or remove any child components directly using the normal Component::addChildComponent() methods).Parameters

 newContentComponent the component to add to this SidePanel, or nullptr to remove the current component. 
 
 deleteComponentWhenNoLongerNeeded if true, the component will be deleted automatically when the SidePanel is deleted or when a different component is added. If false, the caller must manage the lifetime of the component 



See alsogetContent