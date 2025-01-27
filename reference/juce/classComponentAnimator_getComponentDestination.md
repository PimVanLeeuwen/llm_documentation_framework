#### getComponentDestination()


 Rectangle< int > ComponentAnimator::getComponentDestination ( Component \* component ) 
 

Returns the destination position for a component.If the component is being animated, this will return the target position that was specified when animateComponent() was called.If the specified component isn't currently being animated, this method will just return its current position.