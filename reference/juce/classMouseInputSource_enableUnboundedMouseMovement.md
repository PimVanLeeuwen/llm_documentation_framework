#### enableUnboundedMouseMovement()


 void MouseInputSource::enableUnboundedMouseMovement ( bool isEnabled, 
 
 bool keepCursorVisibleUntilOffscreen = false ) const 

Allows the mouse to move beyond the edges of the screen.Calling this method when the mouse button is currently pressed will remove the cursor from the screen and allow the mouse to (seem to) move beyond the edges of the screen.This means that the coordinates returned to mouseDrag() will be unbounded, and this can be used for things like custom slider controls or dragging objects around, where movement would be otherwise be limited by the mouse hitting the edges of the screen.The unbounded mode is automatically turned off when the mouse button is released, or it can be turned off explicitly by calling this method again.Parameters

 isEnabled whether to turn this mode on or off 
 
 keepCursorVisibleUntilOffscreen if set to false, the cursor will immediately be hidden; if true, it will only be hidden when it is moved beyond the edge of the screen