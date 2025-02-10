#### windowControlClickedClose()


 virtual void Component::windowControlClickedClose ( ) virtual 
 

For components that are added to the desktop, this may be called to indicate that the mouse was clicked inside the area of the "close" control.This is currently only called on Windows.This is called by the peer. Component subclasses may override this but should not call it directly.