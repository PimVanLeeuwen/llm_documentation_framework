#### getChildFocus()


 AccessibilityHandler \* AccessibilityHandler::getChildFocus ( ) 
 

Returns the deepest UI element which currently has focus.This can be a child of this UI element or, if no child is focused, this element itself.Note that this can be different to the value of the Component with keyboard focus returned by Component::getCurrentlyFocusedComponent().See alsohasFocus