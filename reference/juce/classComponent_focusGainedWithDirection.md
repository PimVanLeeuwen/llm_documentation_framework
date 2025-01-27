#### focusGainedWithDirection()


 virtual void Component::focusGainedWithDirection ( FocusChangeType cause, FocusChangeDirection direction ) virtual 
 

Called to indicate that this component has just acquired the keyboard focus.This function is called every time focusGained() is called but it has an additional change direction parameter.See alsofocusLost, setWantsKeyboardFocus, getCurrentlyFocusedComponent, hasKeyboardFocus Reimplemented in WebBrowserComponent, and XEmbedComponent.