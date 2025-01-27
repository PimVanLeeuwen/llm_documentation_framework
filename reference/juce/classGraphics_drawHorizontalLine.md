#### drawHorizontalLine()


 void Graphics::drawHorizontalLine ( int y, 
 
 float left, 
 float right ) const 

Draws a horizontal line of pixels at a given y position.The y position is an integer, but the left and right ends of the line can be subpixel positions, and these will be antialiased if necessary.The right parameter must be greater than or equal to the left parameter.