#### eventComponent


 Component\* const MouseEvent::eventComponent 
 

The component that this event applies to.This is usually the component that the mouse was over at the time, but for mousedrag events the mouse could actually be over a different component and the events are still sent to the component that the button was originally pressed on.The x and y member variables are relative to this component's position.If you use getEventRelativeTo() to retarget this object to be relative to a different component, this pointer will be updated, but originalComponent remains unchanged.See alsooriginalComponent