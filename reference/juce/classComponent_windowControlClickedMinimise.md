#### windowControlClickedMinimise()


 virtual void Component::windowControlClickedMinimise ( ) virtual 
 

For components that are added to the desktop, this may be called to indicate that the mouse was clicked inside the area of the "minimise" control.This is currently only called on Windows.This is called by the peer. Component subclasses may override this but should not call it directly.