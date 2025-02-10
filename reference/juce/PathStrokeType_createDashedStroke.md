#### createDashedStroke()


 void PathStrokeType::createDashedStroke ( Path & destPath, 
 
 const Path & sourcePath, 
 const float \* dashLengths, 
 int numDashLengths, 
 const AffineTransform & transform = AffineTransform(), 
 float extraAccuracy = 1.0f ) const 

Applies this stroke type to a path, creating a dashed line.This is similar to createStrokedPath, but uses the array passed in to break the stroke up into a series of dashes.Parameters

 destPath the resultant stroked outline shape will be copied into this path. Note that it's ok for the source and destination Paths to be the same object, so you can easily turn a path into a stroked version of itself. 
 
 sourcePath the path to use as the source 
 dashLengths An array of alternating on/off lengths. E.g. { 2, 3, 4, 5 } will create a line of length 2, then skip a length of 3, then add a line of length 4, skip 5, and keep repeating this pattern. 
 numDashLengths The number of lengths in the dashLengths array. This should really be an even number, otherwise the pattern will get out of step as it repeats. 
 transform an optional transform to apply to the points from the source path as they are being used 
 extraAccuracy if this is greater than 1.0, it will subdivide the path to a higher resolution, which improves the quality if you'll later want to enlarge the stroked path. So for example, if you're planning on drawing the stroke at 3x the size that you're creating it, you should set this to 3.