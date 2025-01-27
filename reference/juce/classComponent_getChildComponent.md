#### getChildComponent()


 Component \* Component::getChildComponent ( int index ) const noexcept 
 

Returns one of this component's child components, by it index.The component with index 0 is at the back of the zorder, the one at the front will have index (getNumChildComponents() 1).If the index is outofrange, this will return a null pointer.See alsogetChildren, getNumChildComponents, getIndexOfChildComponent