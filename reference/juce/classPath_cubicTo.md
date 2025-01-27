#### cubicTo() [2/2]


 void Path::cubicTo ( Point< float > controlPoint1, 
 
 Point< float > controlPoint2, 
 Point< float > endPoint ) 

Adds a cubic bezier curve from the shape's last position to a new position.This will connect the endpoint of the last line or curve that was added to a new point, using a cubic spline with two controlpoints.See the class description for an example of how to add lines and curves to a path.See alsostartNewSubPath, lineTo, quadraticTo, closeSubPath