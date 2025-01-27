#### addBubble()


 void Path::addBubble ( Rectangle< float > bodyArea, 
 
 Rectangle< float > maximumArea, 
 Point< float > arrowTipPosition, 
 float cornerSize, 
 float arrowBaseWidth ) 

Adds a speechbubble shape to the path.Parameters

 bodyArea the area of the body of the bubble shape 
 
 maximumArea an area which encloses the body area and defines the limits within which the arrow tip can be drawn if the tip lies outside this area, the bubble will be drawn without an arrow 
 arrowTipPosition the location of the tip of the arrow 
 cornerSize the size of the rounded corners 
 arrowBaseWidth the width of the base of the arrow where it joins the main rectangle