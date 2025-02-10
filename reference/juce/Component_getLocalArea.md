#### getLocalArea() [2/2]


 Rectangle< float > Component::getLocalArea ( const Component \* sourceComponent, 
 
 Rectangle< float > areaRelativeToSourceComponent ) const 

Converts a rectangle to be relative to this component's coordinate space.This takes a rectangle that is relative to a different component, and returns its position relative to this component. If the sourceComponent parameter is null, the source rectangle is assumed to be a screen coordinate.If you've used setTransform() to apply one or more transforms to components, then the source rectangle may not actually be rectangular when converted to the target space, so in that situation this will return the smallest rectangle that fully contains the transformed area.