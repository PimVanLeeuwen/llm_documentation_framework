#### focusOfChildComponentChanged()


 virtual void Component::focusOfChildComponentChanged ( FocusChangeType cause ) virtual 
 

Called to indicate a change in whether or not this component is the parent of the currentlyfocused component.Essentially this is called when the return value of a call to hasKeyboardFocus (true) has changed. It happens when focus moves from one of this component's children (at any depth) to a component that isn't contained in this one, (or viceversa). Note that this method does NOT get called to when focus simply moves from one of its child components to another.See alsofocusGained, setWantsKeyboardFocus, getCurrentlyFocusedComponent, hasKeyboardFocus Reimplemented in Slider, and TopLevelWindow.