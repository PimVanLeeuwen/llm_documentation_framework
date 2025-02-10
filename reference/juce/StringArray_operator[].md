#### operator[]()


 const String & StringArray::operator[] ( int index ) const noexcept 
 

Returns one of the strings from the array.If the index is outofrange, an empty string is returned.Obviously the reference returned shouldn't be stored for later use, as the string it refers to may disappear when the array changes.