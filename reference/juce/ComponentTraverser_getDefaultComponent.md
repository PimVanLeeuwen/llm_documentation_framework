#### getDefaultComponent()


 virtual Component \* ComponentTraverser::getDefaultComponent ( Component \* parentComponent ) pure virtual 
 

Returns the component that should be used as the traversal entry point within the given parent component.This must return nullptr if there is no default component.Implemented in FocusTraverser, and KeyboardFocusTraverser.