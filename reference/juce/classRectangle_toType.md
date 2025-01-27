#### toType()


template<typename ValueType > 
template<typename TargetType > 

 Rectangle< TargetType > Rectangle< ValueType >::toType ( ) const noexcept 
 

Casts this rectangle to a Rectangle with the given type.If the target type is a conversion from float to int, then the conversion will be done using getSmallestIntegerContainer().