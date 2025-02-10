#### getLocalPoint() [2/2]


 Point< float > Component::getLocalPoint ( const Component \* sourceComponent, 
 
 Point< float > pointRelativeToSourceComponent ) const 

Converts a point to be relative to this component's coordinate space.This takes a point relative to a different component, and returns its position relative to this component. If the sourceComponent parameter is null, the source point is assumed to be a global screen coordinate.