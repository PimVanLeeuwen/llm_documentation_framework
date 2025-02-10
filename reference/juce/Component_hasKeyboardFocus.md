#### hasKeyboardFocus()


 bool Component::hasKeyboardFocus ( bool trueIfChildIsFocused ) const 
 

Returns true if this component currently has the keyboard focus.Parameters

 trueIfChildIsFocused if this is true, then the method returns true if either this component or any of its children (recursively) have the focus. If false, the method only returns true if this component has the focus. 
 



See alsograbKeyboardFocus, giveAwayKeyboardFocus, setWantsKeyboardFocus, getCurrentlyFocusedComponent, focusGained, focusLost