#### getPointOnCircumference() [2/2]


template<typename ValueType > 

 Point< FloatType > Point< ValueType >::getPointOnCircumference ( float radiusX, float radiusY, float angle ) const noexcept 
 

Taking this point to be the centre of an ellipse, this returns a point on its circumference.Parameters

 radiusX the horizontal radius of the circle. 
 
 radiusY the vertical radius of the circle. 
 angle the angle of the point, in radians clockwise from the 12 o'clock position. 


References Point, x, and y.