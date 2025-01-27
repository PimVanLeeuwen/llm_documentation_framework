#### intersectsLine()


 bool Path::intersectsLine ( Line< float > line, 
 
 float tolerance = defaultToleranceForTesting ) const 

Checks whether a line crosses the path.This will return positive if the line crosses any of the paths constituent lines or curves. It doesn't take into account whether the line is inside or outside the path, or whether the path is open or closed.The tolerance parameter is the maximum error allowed when flattening the path, so this method could return a false positive when your point is up to this distance outside the path's boundary.