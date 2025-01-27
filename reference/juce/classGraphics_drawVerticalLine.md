#### drawVerticalLine()


 void Graphics::drawVerticalLine ( int x, 
 
 float top, 
 float bottom ) const 

Draws a vertical line of pixels at a given x position.The x position is an integer, but the top and bottom of the line can be subpixel positions, and these will be antialiased if necessary.The bottom parameter must be greater than or equal to the top parameter.