#### getLastMouseDownPosition()


 static Point< int > Desktop::getLastMouseDownPosition ( ) static 
 

Returns the last position at which a mouse button was pressed.Note that this is just a shortcut for calling getMainMouseSource().getLastMouseDownPosition(), and in a multitouch environment, it doesn't make much sense. ALWAYS prefer to get this information via other means, such as MouseEvent::getMouseDownScreenPosition() if possible, and only ever call this as a last resort.