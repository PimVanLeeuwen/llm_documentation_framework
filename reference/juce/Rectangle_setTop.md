#### setTop()


template<typename ValueType > 

 void Rectangle< ValueType >::setTop ( ValueType newTop ) noexcept 
 

Moves the y position, adjusting the height so that the bottom edge remains in the same place.If the y is moved to be below the current bottom edge, the height will be set to zero.See alsowithTop References jmax().