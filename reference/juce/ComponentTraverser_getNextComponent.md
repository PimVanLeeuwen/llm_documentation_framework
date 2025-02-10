#### getNextComponent()


 virtual Component \* ComponentTraverser::getNextComponent ( Component \* current ) pure virtual 
 

Returns the component that comes after the specified one when moving "forwards".This must return nullptr if there is no next component.Implemented in FocusTraverser, and KeyboardFocusTraverser.