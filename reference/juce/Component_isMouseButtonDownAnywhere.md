#### isMouseButtonDownAnywhere()


 static bool JUCE\_CALLTYPE Component::isMouseButtonDownAnywhere ( ) staticnoexcept 
 

Returns true if a mouse button is currently down.Unlike isMouseButtonDown, this will test the current state of the buttons without regard to which component (if any) it has been pressed in.See alsoisMouseButtonDown, ModifierKeys Referenced by LassoComponent< SelectableItemType >::paint().