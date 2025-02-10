#### showWaitCursor()


 static void MouseCursor::showWaitCursor ( ) static 
 

Makes the system show its default 'busy' cursor.This will turn the system cursor to an hourglass or spinning beachball until the next time the mouse is moved, or hideWaitCursor() is called.This is handy if the message loop is about to block for a couple of seconds while busy and you want to give the user feedback about this.