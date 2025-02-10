#### addCentredArc()


 void Path::addCentredArc ( float centreX, 
 
 float centreY, 
 float radiusX, 
 float radiusY, 
 float rotationOfEllipse, 
 float fromRadians, 
 float toRadians, 
 bool startAsNewSubPath = false ) 

Adds an arc which is centred at a given point, and can have a rotation specified.Note that when specifying the start and end angles, the curve will be drawn either clockwise or anticlockwise according to whether the end angle is greater than the start. This means that sometimes you may need to use values greater than 2\*Pi for the end angle.Parameters

 centreX the centre x of the ellipse 
 
 centreY the centre y of the ellipse 
 radiusX the horizontal radius of the ellipse 
 radiusY the vertical radius of the ellipse 
 rotationOfEllipse an angle by which the whole ellipse should be rotated about its centre, in radians (clockwise) 
 fromRadians the angle (clockwise) in radians at which to start the arc segment (where 0 is the topcentre of the ellipse) 
 toRadians the angle (clockwise) in radians at which to end the arc segment (where 0 is the topcentre of the ellipse). This angle can be greater than 2\*Pi, so for example to draw a curve clockwise from the 9 o'clock position to the 3 o'clock position via 12 o'clock, you'd use 1.5\*Pi and 2.5\*Pi as the start and finish points. 
 startAsNewSubPath if true, the arc will begin a new subpath from its starting point; if false, it will be added to the current subpath, continuing from the current position 



See alsoaddArc, arcTo