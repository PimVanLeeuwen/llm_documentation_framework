#### setViewportIgnoreDragFlag()


 void Component::setViewportIgnoreDragFlag ( bool ignoreDrag ) noexcept 
 

Sets a flag to indicate whether mouse drag events on this Component should be ignored when it is inside a Viewport with dragtoscroll functionality enabled.This is useful for Components such as sliders that should not move when their parent Viewport when dragged.