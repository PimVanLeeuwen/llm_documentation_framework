#### getProportion()


template<typename ValueType > 
template<typename FloatType > 

 Rectangle Rectangle< ValueType >::getProportion ( Rectangle< FloatType > proportionalRect ) const noexcept 
 

Returns a rectangle based on some proportional coordinates relative to this one.So for example getProportion ({ 0.25f, 0.25f, 0.5f, 0.5f }) would return a rectangle of half the original size, with the same centre.References Rectangle< ValueType >::proportionOfHeight(), and Rectangle< ValueType >::proportionOfWidth().