#### addPieSegment() [2/2]


 void Path::addPieSegment ( Rectangle< float > segmentBounds, 
 
 float fromRadians, 
 float toRadians, 
 float innerCircleProportionalSize ) 

Adds a "piechart" shape to the path.The shape is added as a new subpath. (Any currently open paths will be left open).Note that when specifying the start and end angles, the curve will be drawn either clockwise or anticlockwise according to whether the end angle is greater than the start. This means that sometimes you may need to use values greater than 2\*Pi for the end angle.Parameters

 segmentBounds the outer rectangle in which the elliptical outline fits 
 
 fromRadians the angle (clockwise) in radians at which to start the arc segment (where 0 is the topcentre of the ellipse) 
 toRadians the angle (clockwise) in radians at which to end the arc segment (where 0 is the topcentre of the ellipse) 
 innerCircleProportionalSize if this is > 0, then the pie will be drawn as a curved band around a hollow ellipse at its centre, where this value indicates the inner ellipse's size with respect to the outer one. 



See alsoaddArc