#### createFocusTraverser()


 virtual std::unique\_ptr< ComponentTraverser > Component::createFocusTraverser ( ) virtual 
 

Creates a ComponentTraverser object to determine the logic by which focus should be passed from this component.The default implementation of this method will return an instance of FocusTraverser if this component is a focus container (as determined by the setFocusContainerType() method). If the component isn't a focus container, then it will recursively call createFocusTraverser() on its parents.If you override this to return a custom traverser object, then this component and all its subcomponents will use the new object to make their focusing decisions.