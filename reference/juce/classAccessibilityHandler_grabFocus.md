#### grabFocus()


 void AccessibilityHandler::grabFocus ( ) 
 

Tries to give focus to this UI element.If the UI element is focusable and not ignored this will update the currently focused element, try to give keyboard focus to the Component it represents, and notify any listening accessibility clients that the current focus has changed.See alsohasFocus, giveAwayFocus