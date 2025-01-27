#### setTopRightPosition()


 void Component::setTopRightPosition ( int x, 
 
 int y ) 

Moves the component to a new position.Changes the position of the component's topright corner (keeping it the same size). The position is relative to the topleft of the component's parent.If the component actually moves, this method will make a synchronous call to moved().Note that if you've used setTransform() to apply a transform, then the component's bounds will no longer be a direct reflection of the position at which it appears within its parent, as the transform will be applied to whatever bounds you set for it.