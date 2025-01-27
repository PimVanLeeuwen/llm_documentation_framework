#### findControlAtPoint()


 virtual WindowControlKind Component::findControlAtPoint ( Point< float > ) const virtual 
 

For components that are added to the desktop, this may be called to determine what kind of control is at particular locations in the window.On Windows, this is used to provide functionality like Aero Snap (snapping the window to half of the screen after dragging the window's caption area to the edge of the screen), doubleclicking a horizontal border to stretch a window vertically, and the window tiling flyout that appears when hovering the mouse over the maximise button.It's dangerous to call Component::contains from an overriding function, because this might call into the peer to do system hittesting but the system hittest could in turn call findControlAtPoint, leading to infinite recursion. It's better to use functions like Rectangle::contains or Path::contains to test for the window control areas.This is called by the peer. Component subclasses may override this but should not call it directly.