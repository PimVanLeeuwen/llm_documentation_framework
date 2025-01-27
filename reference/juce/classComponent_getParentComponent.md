#### getParentComponent()


 Component \* Component::getParentComponent ( ) const noexcept 
 

Returns the component which this component is inside.If this is the highestlevel component or hasn't yet been added to a parent, this will return null.Referenced by LassoComponent< SelectableItemType >::beginLasso().