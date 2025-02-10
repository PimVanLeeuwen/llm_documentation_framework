#### getMousePosition()


 static Point< int > Desktop::getMousePosition ( ) static 
 

Returns the mouse position.The coordinates are relative to the topleft of the main monitor.Note that this is just a shortcut for calling getMainMouseSource().getScreenPosition(), and you should only resort to grabbing the global mouse position if there's really no way to get the coordinates via a mouse event callback instead.