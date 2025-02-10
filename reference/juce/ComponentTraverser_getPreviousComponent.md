#### getPreviousComponent()


 virtual Component \* ComponentTraverser::getPreviousComponent ( Component \* current ) pure virtual 
 

Returns the component that comes after the specified one when moving "backwards".This must return nullptr if there is no previous component.Implemented in FocusTraverser, and KeyboardFocusTraverser.