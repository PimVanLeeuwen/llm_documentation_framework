#### toString()


template<typename ValueType > 

 String Rectangle< ValueType >::toString ( ) const 
 

Creates a string describing this rectangle.The string will be of the form "x y width height", e.g. "100 100 400 200".Coupled with the fromString() method, this is very handy for things like storing rectangles (particularly component positions) in XML attributes.See alsofromString References String::preallocateBytes().