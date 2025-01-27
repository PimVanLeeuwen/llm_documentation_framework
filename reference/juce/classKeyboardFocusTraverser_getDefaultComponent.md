#### getDefaultComponent()


 Component \* KeyboardFocusTraverser::getDefaultComponent ( Component \* parentComponent ) overridevirtual 
 

Returns the component that should receive keyboard focus by default within the given parent component.The default implementation will return the foremost focusable component (as determined by FocusTraverser) that also wants keyboard focus, or nullptr if there is no suitable component.Implements ComponentTraverser.