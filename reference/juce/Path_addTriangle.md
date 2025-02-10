#### addTriangle() [2/2]


 void Path::addTriangle ( Point< float > point1, 
 
 Point< float > point2, 
 Point< float > point3 ) 

Adds a triangle to the path.The triangle is added as a new closed subpath. (Any currently open paths will be left open).Note that whether the vertices are specified in clockwise or anticlockwise order will affect how the triangle is filled when it overlaps other shapes (the winding order setting will affect this of course).