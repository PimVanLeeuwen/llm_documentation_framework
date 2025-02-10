#### operator[]() [2/2]


 JSObject JSObject::operator[] ( int64 index ) const 
 

Returns a new cursor object pointing to the specified element in an Array.This function is a shorthand for getChild (int64).You must ensure that the cursor points to an Array before calling this function.See alsoisArray