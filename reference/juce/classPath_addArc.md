#### addArc()


 void Path::addArc ( float x, 
 
 float y, 
 float width, 
 float height, 
 float fromRadians, 
 float toRadians, 
 bool startAsNewSubPath = false ) 

Adds an elliptical arc to the current path.Note that when specifying the start and end angles, the curve will be drawn either clockwise or anticlockwise according to whether the end angle is greater than the start. This means that sometimes you may need to use values greater than 2\*Pi for the end angle.Parameters

 x the lefthand edge of the rectangle in which the elliptical outline fits 
 
 y the top edge of the rectangle in which the elliptical outline fits 
 width the width of the rectangle in which the elliptical outline fits 
 height the height of the rectangle in which the elliptical outline fits 
 fromRadians the angle (clockwise) in radians at which to start the arc segment (where 0 is the topcentre of the ellipse) 
 toRadians the angle (clockwise) in radians at which to end the arc segment (where 0 is the topcentre of the ellipse). This angle can be greater than 2\*Pi, so for example to draw a curve clockwise from the 9 o'clock position to the 3 o'clock position via 12 o'clock, you'd use 1.5\*Pi and 2.5\*Pi as the start and finish points. 
 startAsNewSubPath if true, the arc will begin a new subpath from its starting point; if false, it will be added to the current subpath, continuing from the current position 



See alsoaddCentredArc, arcTo, addPieSegment, addEllipse