#### getBoundsInParent()


 Rectangle< int > Component::getBoundsInParent ( ) const noexcept 
 

Returns the area of this component's parent which this component covers.The returned area is relative to the parent's coordinate space. If the component has an affine transform specified, then the resulting area will be the smallest rectangle that fully covers the component's transformed bounding box. If this component has no parent, the return value will simply be the same as getBounds().