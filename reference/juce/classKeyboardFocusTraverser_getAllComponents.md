#### getAllComponents()


 std::vector< Component \* > KeyboardFocusTraverser::getAllComponents ( Component \* parentComponent ) overridevirtual 
 

Returns all of the components that can receive keyboard focus within the given parent component in traversal order.The default implementation will return all focusable child components (as determined by FocusTraverser) that also wants keyboard focus.Implements ComponentTraverser.