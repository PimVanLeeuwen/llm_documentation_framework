#### lineTo() [2/2]


 void Path::lineTo ( Point< float > end ) 
 

Adds a line from the shape's last position to a new endpoint.This will connect the endpoint of the last line or curve that was added to a new point, using a straight line.See the class description for an example of how to add lines and curves to a path.See alsostartNewSubPath, quadraticTo, cubicTo, closeSubPath