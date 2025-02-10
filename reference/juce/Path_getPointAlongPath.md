#### getPointAlongPath()


 Point< float > Path::getPointAlongPath ( float distanceFromStart, 
 
 const AffineTransform & transform = AffineTransform(), 
 float tolerance = defaultToleranceForMeasurement ) const 

Returns a point that is the specified distance along the path.If the distance is greater than the total length of the path, this will return the end point.See alsogetLength