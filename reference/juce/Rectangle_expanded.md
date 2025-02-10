#### expanded() [2/2]


template<typename ValueType > 

 Rectangle Rectangle< ValueType >::expanded ( ValueType delta ) const nodiscardnoexcept 
 

Returns a rectangle that is larger than this one by a given amount.Effectively, the rectangle returned is (x delta, y delta, w + delta \* 2, h + delta \* 2).See alsoexpand, reduce, reduced References Rectangle< ValueType >::expanded().