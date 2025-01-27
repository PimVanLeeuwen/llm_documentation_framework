#### getPreviousComponent()


 Component \* KeyboardFocusTraverser::getPreviousComponent ( Component \* current ) overridevirtual 
 

Returns the component that should be given keyboard focus after the specified one when moving "backwards".The default implementation will return the previous focusable component (as determined by FocusTraverser) that also wants keyboard focus, or nullptr if there is no suitable component.Implements ComponentTraverser.