#### equalsWithSameType()


 bool var::equalsWithSameType ( const var & other ) const noexcept 
 

Returns true if this var has the same value and type as the one supplied.This differs from equals() because e.g. "123" and 123 will be considered different.See alsoequals