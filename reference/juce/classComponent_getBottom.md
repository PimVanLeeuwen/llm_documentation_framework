#### getBottom()


 int Component::getBottom ( ) const noexcept 
 

Returns the y coordinate of the bottom edge of this component.This is a distance in pixels from the top edge of the component's parent.Note that if you've used setTransform() to apply a transform, then the component's bounds will no longer be a direct reflection of the position at which it appears within its parent, as the transform will be applied to its bounding box.