#### localAreaToGlobal() [2/2]


 Rectangle< float > Component::localAreaToGlobal ( Rectangle< float > localArea ) const 
 

Converts a rectangle from this component's coordinate space to a screen coordinate.If you've used setTransform() to apply one or more transforms to components, then the source rectangle may not actually be rectangular when converted to the target space, so in that situation this will return the smallest rectangle that fully contains the transformed area.See alsogetLocalPoint, localPointToGlobal