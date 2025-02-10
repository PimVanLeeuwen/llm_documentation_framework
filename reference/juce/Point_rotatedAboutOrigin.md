#### rotatedAboutOrigin()


template<typename ValueType > 
template<typename T = ValueType, std::enable\_if\_t< std::is\_floating\_point\_v< T >, int > = 0> 

 Point Point< ValueType >::rotatedAboutOrigin ( ValueType angleRadians ) const noexcept 
 

Returns the point that would be reached by rotating this point clockwise about the origin by the specified angle.References Point, x, and y.