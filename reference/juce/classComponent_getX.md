#### getX()


 int Component::getX ( ) const noexcept 
 

Returns the x coordinate of the component's left edge.This is a distance in pixels from the left edge of the component's parent.Note that if you've used setTransform() to apply a transform, then the component's bounds will no longer be a direct reflection of the position at which it appears within its parent, as the transform will be applied to its bounding box.Referenced by StandaloneFilterWindow::~StandaloneFilterWindow().