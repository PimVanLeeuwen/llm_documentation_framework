#### setFixedAspectRatio()


 void ComponentBoundsConstrainer::setFixedAspectRatio ( double widthOverHeight ) noexcept 
 

Specifies a widthtoheight ratio that the resizer should always maintain.If the value is 0, no aspect ratio is enforced. If it's nonzero, the width will always be maintained as this multiple of the height.See alsosetResizeLimits