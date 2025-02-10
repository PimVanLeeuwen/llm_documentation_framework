#### giveAwayKeyboardFocus()


 void Component::giveAwayKeyboardFocus ( ) 
 

If this component or any of its children currently have the keyboard focus, this will defocus it, send a focus change notification, and try to pass the focus to the next component.See alsograbKeyboardFocus, setWantsKeyboardFocus, getCurrentlyFocusedComponent, focusGained, focusLost