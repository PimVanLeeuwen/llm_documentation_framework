#### drawDashedLine()


 void Graphics::drawDashedLine ( Line< float > line, 
 
 const float \* dashLengths, 
 int numDashLengths, 
 float lineThickness = 1.0f, 
 int dashIndexToStartFrom = 0 ) const 

Draws a dashed line using a custom set of dashlengths.Parameters

 line the line to draw 
 
 dashLengths a series of lengths to specify the on/off lengths e.g. { 4, 5, 6, 7 } will draw a line of 4 pixels, skip 5 pixels, draw 6 pixels, skip 7 pixels, and then repeat. 
 numDashLengths the number of elements in the array (this must be an even number). 
 lineThickness the thickness of the line to draw 
 dashIndexToStartFrom the index in the dashlength array to use for the first segment 



See alsoPathStrokeType::createDashedStroke