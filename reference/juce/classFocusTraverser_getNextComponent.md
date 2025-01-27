#### getNextComponent()


 Component \* FocusTraverser::getNextComponent ( Component \* current ) overridevirtual 
 

Returns the component that should be given focus after the specified one when moving "forwards".The default implementation will return the next visible and enabled component which is to the right of or below this one, and will return nullptr if there is no suitable component.Implements ComponentTraverser.