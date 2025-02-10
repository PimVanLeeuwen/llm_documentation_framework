#### getAngleToPoint()


template<typename ValueType > 

 FloatType Point< ValueType >::getAngleToPoint ( Point< ValueType > other ) const noexcept 
 

Returns the angle from this point to another one.Taking this point to be the centre of a circle, and the other point being a position on the circumference, the return value is the number of radians clockwise from the 12 o'clock direction. So 12 o'clock = 0, 3 o'clock = Pi/2, 6 o'clock = Pi, 9 o'clock = Pi/2References x, and y.