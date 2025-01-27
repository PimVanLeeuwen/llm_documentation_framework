#### operator[]()


 const var & ValueTree::operator[] ( const Identifier & name ) const noexcept 
 

Returns the value of a named property.If no such property has been set, this will return a void variant. This is the same as calling getProperty().See alsogetProperty