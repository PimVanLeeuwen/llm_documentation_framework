#### getAllComponents()


 std::vector< Component \* > FocusTraverser::getAllComponents ( Component \* parentComponent ) overridevirtual 
 

Returns all of the components that can receive focus within the given parent component in traversal order.The default implementation will return all visible and enabled child components.Implements ComponentTraverser.