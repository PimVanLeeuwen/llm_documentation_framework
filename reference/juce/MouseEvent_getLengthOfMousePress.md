#### getLengthOfMousePress()


 int MouseEvent::getLengthOfMousePress ( ) const noexcept 
 

Returns the time that the mouse button has been held down for.If called from a mouseDrag or mouseUp callback, this will return the number of milliseconds since the corresponding mouseDown event occurred. If called in other contexts, e.g. a mouseMove, then the returned value may be 0 or an undefined value.