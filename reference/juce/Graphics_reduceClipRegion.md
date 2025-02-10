#### reduceClipRegion() [5/5]


 bool Graphics::reduceClipRegion ( const Image & image, 
 
 const AffineTransform & transform ) 

Intersects the current clipping region with an image's alphachannel.The current clipping path is intersected with the area covered by this image's alphachannel, after the image has been transformed by the specified matrix.Parameters

 image the image whose alphachannel should be used. If the image doesn't have an alphachannel, it is treated as entirely opaque. 
 
 transform a matrix to apply to the image 



Returnstrue if the resulting clipping region is nonzero in size 
See alsoreduceClipRegion