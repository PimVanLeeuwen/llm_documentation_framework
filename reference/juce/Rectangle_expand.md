#### expand()


template<typename ValueType > 

 void Rectangle< ValueType >::expand ( ValueType deltaX, ValueType deltaY ) noexcept 
 

Expands the rectangle by a given amount.Effectively, its new size is (x deltaX, y deltaY, w + deltaX \* 2, h + deltaY \* 2).See alsoexpanded, reduce, reduced References jmax(), and Rectangle< ValueType >::setBounds().Referenced by Rectangle< ValueType >::reduce().