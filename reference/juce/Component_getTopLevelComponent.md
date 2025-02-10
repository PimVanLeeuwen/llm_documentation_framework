#### getTopLevelComponent()


 Component \* Component::getTopLevelComponent ( ) const noexcept 
 

Returns the highestlevel component which contains this one or its parents.This will search upwards in the parenthierarchy from this component, until it finds the highest one that doesn't have a parent (i.e. is on the desktop or not yet added to a parent), and will return that.