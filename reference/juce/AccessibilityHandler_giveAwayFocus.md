#### giveAwayFocus()


 void AccessibilityHandler::giveAwayFocus ( ) const 
 

If this UI element or any of its children in the accessibility hierarchy currently have focus, this will defocus it.This will also give away the keyboard focus from the Component it represents, and notify any listening accessibility clients that the current focus has changed.See alsohasFocus, grabFocus