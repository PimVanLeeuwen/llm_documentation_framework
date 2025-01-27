#### getVarPointer() [2/2]


 const var \* NamedValueSet::getVarPointer ( const Identifier & name ) const noexcept 
 

Returns a pointer to the var that holds a named value, or null if there is no value with this name.Do not use this method unless you really need access to the internal var object for some reason for normal reading and writing always prefer operator[]() and set(). Also note that the pointer returned may become invalid as soon as any subsequent methods are called on the NamedValueSet.