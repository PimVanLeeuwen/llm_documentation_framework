#### expanded()


template<typename ValueType > 

 Range Range< ValueType >::expanded ( ValueType amount ) const nodiscardconstexprnoexcept 
 

Returns a range which has its start moved down and its end moved up by the given amount.ReturnsThe returned range will be (start amount, end + amount) References Range< ValueType >::Range().