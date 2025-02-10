#### getIndexOfChildComponent()


 int Component::getIndexOfChildComponent ( const Component \* child ) const noexcept 
 

Returns the index of this component in the list of child components.A value of 0 means it is first in the list (i.e. behind all other components). Higher values are further towards the front.Returns 1 if the component passedin is not a child of this component.See alsogetChildren, getNumChildComponents, getChildComponent, addChildComponent, toFront, toBack, toBehind