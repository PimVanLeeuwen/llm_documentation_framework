#### contains() [2/2]


 bool Path::contains ( Point< float > point, 
 
 float tolerance = defaultToleranceForTesting ) const 

Checks whether a point lies within the path.This is only relevant for closed paths (see closeSubPath()), and may produce false results if used on a path which has open subpaths.The path's winding rule is taken into account by this method.The tolerance parameter is the maximum error allowed when flattening the path, so this method could return a false positive when your point is up to this distance outside the path's boundary.See alsocloseSubPath, setUsingNonZeroWinding