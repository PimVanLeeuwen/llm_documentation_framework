#### addRoundedRectangle() [5/5]


template<typename ValueType > 

 void Path::addRoundedRectangle ( Rectangle< ValueType > rectangle, 
 
 float cornerSize ) 

Adds a rectangle with rounded corners to the path.The rectangle is added as a new subpath. (Any currently open paths will be left open).See alsoaddRectangle, addTriangle