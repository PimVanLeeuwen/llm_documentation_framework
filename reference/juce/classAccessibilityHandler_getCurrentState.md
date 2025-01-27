#### getCurrentState()


 virtual AccessibleState AccessibilityHandler::getCurrentState ( ) const virtual 
 

Returns the current state of the UI element.The default implementation of this method will set the focusable flag and, if this UI element is currently focused, will also set the focused flag.