#### updateMouseCursor()


 void Component::updateMouseCursor ( ) const 
 

Forces the current mouse cursor to be updated.If you're overriding the getMouseCursor() method to control which cursor is displayed, then this will only be checked each time the user moves the mouse. So if you want to force the system to check that the cursor being displayed is uptodate (even if the mouse is just sitting there), call this method.(If you're changing the cursor using setMouseCursor(), you don't need to bother calling this).