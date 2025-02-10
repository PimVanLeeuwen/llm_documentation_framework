#### isParentOf()


 bool Component::isParentOf ( const Component \* possibleChild ) const noexcept 
 

Checks whether a component is anywhere inside this component or its children.This will recursively check through this component's children to see if the given component is anywhere inside.