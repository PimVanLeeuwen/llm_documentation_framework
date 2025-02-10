#### addPath() [2/2]


 void Path::addPath ( const Path & pathToAppend, 
 
 const AffineTransform & transformToApply ) 

Adds another path to this one, transforming it on the way in.The new path is added as a new subpath, its points being transformed by the given matrix before being added.Parameters

 pathToAppend the path to add 
 
 transformToApply an optional transform to apply to the incoming vertices