#### clone()


 var var::clone ( ) const noexcept 
 

Returns a deep copy of this object.For simple types this just returns a copy, but if the object contains any arrays or DynamicObjects, they will be cloned (recursively).