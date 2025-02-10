#### getDefaultComponent()


 Component \* FocusTraverser::getDefaultComponent ( Component \* parentComponent ) overridevirtual 
 

Returns the component that should receive focus by default within the given parent component.The default implementation will just return the foremost visible and enabled child component, and will return nullptr if there is no suitable component.Implements ComponentTraverser.