#### createCubicBezier() [2/2]


 static std::function< float(float)> Easings::createCubicBezier ( Point< float > controlPoint1, Point< float > controlPoint2 ) static 
 

Returns a cubic Bezier function with two control points.These points are the two middle points of a cubic Bezier function's four control points, the first and last being (0, 0), and (1, 1).