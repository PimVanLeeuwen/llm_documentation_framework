#### getBounds()


 Rectangle< int > Component::getBounds ( ) const noexcept 
 

Returns this component's bounding box.The rectangle returned is relative to the topleft of the component's parent.Note that if you've used setTransform() to apply a transform, then the component's bounds will no longer be a direct reflection of the position at which it appears within its parent, as the transform will be applied to its bounding box.Referenced by LassoComponent< SelectableItemType >::dragLasso().