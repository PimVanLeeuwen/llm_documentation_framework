#### operator Type()


template<typename Type > 

 CachedValue< Type >::operator Type ( ) const noexcept 
 

Returns the current value of the property.If the property does not exist, returns the fallback default value.This is the same as calling get().