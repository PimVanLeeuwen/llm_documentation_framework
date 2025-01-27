#### ScopedValueSetter() [2/2]


template<typename ValueType > 

 ScopedValueSetter< ValueType >::ScopedValueSetter ( ValueType & valueToSet, 
 
 ValueType newValue, 
 ValueType valueWhenDeleted ) 

Creates a ScopedValueSetter that will immediately change the specified value to the given new value, and will then reset it to be valueWhenDeleted when this object is deleted.