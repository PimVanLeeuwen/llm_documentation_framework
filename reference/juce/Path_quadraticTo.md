#### quadraticTo() [2/2]


 void Path::quadraticTo ( Point< float > controlPoint, 
 
 Point< float > endPoint ) 

Adds a quadratic bezier curve from the shape's last position to a new position.This will connect the endpoint of the last line or curve that was added to a new point, using a quadratic spline with one controlpoint.See the class description for an example of how to add lines and curves to a path.See alsostartNewSubPath, lineTo, cubicTo, closeSubPath