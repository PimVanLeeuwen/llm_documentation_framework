#### setSize()


 void Component::setSize ( int newWidth, 
 
 int newHeight ) 

Changes the size of the component.A synchronous call to resized() will occur if the size actually changes.Note that if you've used setTransform() to apply a transform, then the component's bounds will no longer be a direct reflection of the position at which it appears within its parent, as the transform will be applied to whatever bounds you set for it.Referenced by LassoComponent< SelectableItemType >::beginLasso().