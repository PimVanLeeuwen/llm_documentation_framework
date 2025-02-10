#### createStrokeWithArrowheads()


 void PathStrokeType::createStrokeWithArrowheads ( Path & destPath, 
 
 const Path & sourcePath, 
 float arrowheadStartWidth, 
 float arrowheadStartLength, 
 float arrowheadEndWidth, 
 float arrowheadEndLength, 
 const AffineTransform & transform = AffineTransform(), 
 float extraAccuracy = 1.0f ) const 

Applies this stroke type to a path and returns the resultant stroke as another Path.Parameters

 destPath the resultant stroked outline shape will be copied into this path. Note that it's ok for the source and destination Paths to be the same object, so you can easily turn a path into a stroked version of itself. 
 
 sourcePath the path to use as the source 
 arrowheadStartWidth the width of the arrowhead at the start of the path 
 arrowheadStartLength the length of the arrowhead at the start of the path 
 arrowheadEndWidth the width of the arrowhead at the end of the path 
 arrowheadEndLength the length of the arrowhead at the end of the path 
 transform an optional transform to apply to the points from the source path as they are being used 
 extraAccuracy if this is greater than 1.0, it will subdivide the path to a higher resolution, which improves the quality if you'll later want to enlarge the stroked path. So for example, if you're planning on drawing the stroke at 3x the size that you're creating it, you should set this to 3. 



See alsocreateDashedStroke