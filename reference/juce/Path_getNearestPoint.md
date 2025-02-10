#### getNearestPoint()


 float Path::getNearestPoint ( Point< float > targetPoint, 
 
 Point< float > & pointOnPath, 
 const AffineTransform & transform = AffineTransform(), 
 float tolerance = defaultToleranceForMeasurement ) const 

Finds the point along the path which is nearest to a given position.This sets pointOnPath to the nearest point, and returns the distance of this point from the start of the path.