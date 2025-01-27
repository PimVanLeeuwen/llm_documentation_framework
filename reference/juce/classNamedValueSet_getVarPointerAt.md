#### getVarPointerAt() [2/2]


 const var \* NamedValueSet::getVarPointerAt ( int index ) const noexcept 
 

Returns the value of the item at a given index.The index must be between 0 and size() 1, or this will return a nullptr Also note that the pointer returned may become invalid as soon as any subsequent methods are called on the NamedValueSet.