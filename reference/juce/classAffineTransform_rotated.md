#### rotated() [2/2]


 AffineTransform AffineTransform::rotated ( float angleInRadians, float pivotX, float pivotY ) const noexcept 
 

Returns a transform which is the same as this one followed by a rotation about a given point.The rotation is specified by a number of radians to rotate clockwise, centred around the coordinates passed in.