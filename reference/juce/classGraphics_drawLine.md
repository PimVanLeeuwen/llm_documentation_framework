#### drawLine() [4/4]


 void Graphics::drawLine ( Line< float > line, 
 
 float lineThickness ) const 

Draws a line between two points with a given thickness.See alsoPath::addLineSegment TIP: If you're trying to draw horizontal or vertical lines, don't use this it's better to use fillRect() instead unless you really need an angled line.