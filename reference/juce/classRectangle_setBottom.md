#### setBottom()


template<typename ValueType > 

 void Rectangle< ValueType >::setBottom ( ValueType newBottom ) noexcept 
 

Adjusts the height so that the bottom edge of the rectangle has this new value.If the new bottom is lower than the current Y value, the Y will be pushed down to match it.See alsogetBottom, withBottom References jmin().