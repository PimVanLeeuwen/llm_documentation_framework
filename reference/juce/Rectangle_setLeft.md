#### setLeft()


template<typename ValueType > 

 void Rectangle< ValueType >::setLeft ( ValueType newLeft ) noexcept 
 

Moves the x position, adjusting the width so that the righthand edge remains in the same place.If the x is moved to be on the right of the current righthand edge, the width will be set to zero.See alsowithLeft References jmax().