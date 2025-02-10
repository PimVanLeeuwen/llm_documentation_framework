#### getUnion()


template<typename ValueType > 

 Rectangle Rectangle< ValueType >::getUnion ( Rectangle< ValueType > other ) const noexcept 
 

Returns the smallest rectangle that contains both this one and the one passedin.If either this or the other rectangle are empty, they will not be counted as part of the resulting region.References Rectangle< ValueType >::isEmpty(), jmax(), and jmin().