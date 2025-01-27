#### addQuadrilateral()


 void Path::addQuadrilateral ( float x1, 
 
 float y1, 
 float x2, 
 float y2, 
 float x3, 
 float y3, 
 float x4, 
 float y4 ) 

Adds a quadrilateral to the path.The quad is added as a new closed subpath. (Any currently open paths will be left open).Note that whether the vertices are specified in clockwise or anticlockwise order will affect how the quad is filled when it overlaps other shapes (the winding order setting will affect this of course).