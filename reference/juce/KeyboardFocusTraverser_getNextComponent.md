#### getNextComponent()


 Component \* KeyboardFocusTraverser::getNextComponent ( Component \* current ) overridevirtual 
 

Returns the component that should be given keyboard focus after the specified one when moving "forwards".The default implementation will return the next focusable component (as determined by FocusTraverser) that also wants keyboard focus, or nullptr if there is no suitable component.Implements ComponentTraverser.