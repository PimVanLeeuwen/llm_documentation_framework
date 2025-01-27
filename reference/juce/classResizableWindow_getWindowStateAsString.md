#### getWindowStateAsString()


 String ResizableWindow::getWindowStateAsString ( ) 
 

Returns a string which encodes the window's current size and position.This string will encapsulate the window's size, position, and whether it's in fullscreen mode. It's intended for letting your application save and restore a window's position.Use the restoreWindowStateFromString() to restore from a saved state.See alsorestoreWindowStateFromString