#### createKeyboardFocusTraverser()


 virtual std::unique\_ptr< ComponentTraverser > Component::createKeyboardFocusTraverser ( ) virtual 
 

Creates a ComponentTraverser object to use to determine the logic by which keyboard focus should be passed from this component.The default implementation of this method will return an instance of KeyboardFocusTraverser if this component is a keyboard focus container (as determined by the setFocusContainerType() method). If the component isn't a keyboard focus container, then it will recursively call createKeyboardFocusTraverser() on its parents.If you override this to return a custom traverser object, then this component and all its subcomponents will use the new object to make their keyboard focusing decisions.Reimplemented in FilenameComponent, and Label.