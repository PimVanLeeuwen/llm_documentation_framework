#### reduce()


template<typename ValueType > 

 void Rectangle< ValueType >::reduce ( ValueType deltaX, ValueType deltaY ) noexcept 
 

Shrinks the rectangle by a given amount.Effectively, its new size is (x + deltaX, y + deltaY, w deltaX \* 2, h deltaY \* 2).See alsoreduced, expand, expanded References Rectangle< ValueType >::expand().