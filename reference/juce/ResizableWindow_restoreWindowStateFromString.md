#### restoreWindowStateFromString()


 bool ResizableWindow::restoreWindowStateFromString ( const String & previousState ) 
 

Restores the window to a previouslysaved size and position.This restores the window's size, position and fullscreen status from an string that was previously created with the getWindowStateAsString() method.Returnsfalse if the string wasn't a valid window state 
See alsogetWindowStateAsString