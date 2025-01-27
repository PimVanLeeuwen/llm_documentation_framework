#### addArrow()


 void Path::addArrow ( Line< float > line, 
 
 float lineThickness, 
 float arrowheadWidth, 
 float arrowheadLength ) 

Adds a line with an arrowhead on the end.The arrow is added as a new closed subpath. (Any currently open paths will be left open).See alsoPathStrokeType::createStrokeWithArrowheads