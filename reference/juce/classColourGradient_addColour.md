#### addColour()


 int ColourGradient::addColour ( double proportionAlongGradient, 
 
 Colour colour ) 

Adds a colour at a point along the length of the gradient.This allows the gradient to go through a spectrum of colours, instead of just a start and end colour.Parameters

 proportionAlongGradient a value between 0 and 1.0, which is the proportion of the distance along the line between the two points at which the colour should occur. 
 
 colour the colour that should be used at this point 



Returnsthe index at which the new point was added