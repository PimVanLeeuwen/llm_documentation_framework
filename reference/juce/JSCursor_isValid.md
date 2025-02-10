#### isValid()


 bool JSCursor::isValid ( ) const 
 

Returns true if the location of the cursor is reachable from the cursor's JSObject root.This means it is safe to call set on this JSCursor and the location will then point to an Object corresponding to the supplied value.It isn't guaranteed that there is already an Object at this location, in which case calling get will return var::undefined().