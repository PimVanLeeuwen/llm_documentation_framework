#### setExplicitFocusOrder()


 void Component::setExplicitFocusOrder ( int newFocusOrderIndex ) 
 

Sets the focus order of this component.The focus order is used by the default traverser implementation returned by createFocusTraverser() as part of its algorithm for deciding the order in which components should be traversed. A value of 0 or less is taken to mean that no explicit order is wanted, and that traversal should use other factors, like the component's position.See alsogetExplicitFocusOrder, FocusTraverser, createFocusTraverser