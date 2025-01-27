#### setWantsKeyboardFocus()


 void Component::setWantsKeyboardFocus ( bool wantsFocus ) noexcept 
 

Sets a flag to indicate whether this component wants keyboard focus or not.By default components aren't actually interested in gaining the keyboard focus, but this method can be used to turn this on.See the grabKeyboardFocus() method for details about the way a component is chosen to receive the focus.See alsograbKeyboardFocus, giveAwayKeyboardFocus, getWantsKeyboardFocus