#### reduced() [2/2]


template<typename ValueType > 

 Rectangle Rectangle< ValueType >::reduced ( ValueType delta ) const nodiscardnoexcept 
 

Returns a rectangle that is smaller than this one by a given amount.Effectively, the rectangle returned is (x + delta, y + delta, w delta \* 2, h delta \* 2).See alsoreduce, expand, expanded References Rectangle< ValueType >::reduced().