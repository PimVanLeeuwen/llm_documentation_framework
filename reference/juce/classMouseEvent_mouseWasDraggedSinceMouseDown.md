#### mouseWasDraggedSinceMouseDown()


 bool MouseEvent::mouseWasDraggedSinceMouseDown ( ) const noexcept 
 

Returns true if the user seems to be performing a drag gesture.This is only meaningful if called in either a mouseUp() or mouseDrag() method.It will return true if the user has dragged the mouse more than a few pixels from the place where the mousedown occurred or the mouse has been held down for a significant amount of time.Once they have dragged it far enough for this method to return true, it will continue to return true until the mouseup, even if they move the mouse back to the same location at which the mousedown happened. This means that it's very handy for objects that can either be clicked on or dragged, as you can use it in the mouseDrag() callback to ignore small movements they might make while trying to click.