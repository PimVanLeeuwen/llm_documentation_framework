#### getPreviousComponent()


 Component \* FocusTraverser::getPreviousComponent ( Component \* current ) overridevirtual 
 

Returns the component that should be given focus after the specified one when moving "backwards".The default implementation will return the previous visible and enabled component which is to the left of or above this one, and will return nullptr if there is no suitable component.Implements ComponentTraverser.