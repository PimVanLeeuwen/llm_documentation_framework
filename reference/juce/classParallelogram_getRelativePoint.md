#### getRelativePoint()


template<typename ValueType > 

 Point< ValueType > Parallelogram< ValueType >::getRelativePoint ( Point< ValueType > relativePosition ) const noexcept 
 

Returns a point within this parallelogram, specified as proportional coordinates.The relative X and Y values should be between 0 and 1, where 0 is the left or top of this parallelogram, and 1 is the right or bottom. (Outofbounds values will return a point outside the parallelogram).References Parallelogram< ValueType >::bottomLeft, Parallelogram< ValueType >::topLeft, and Parallelogram< ValueType >::topRight.