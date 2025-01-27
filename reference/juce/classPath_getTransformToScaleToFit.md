#### getTransformToScaleToFit() [2/2]


 AffineTransform Path::getTransformToScaleToFit ( Rectangle< float > area, 
 
 bool preserveProportions, 
 Justification justificationType = Justification::centred ) const 

Returns a transform that can be used to rescale the path to fit into a given space.Parameters

 area the rectangle to fit the path inside 
 
 preserveProportions if true, it will fit the path into the space without altering its horizontal/vertical scale ratio; if false, it will distort the path to fill the specified ratio both horizontally and vertically 
 justificationType if the proportions are preserved, the resultant path may be smaller than the available rectangle, so this describes how it should be positioned within the space. 



Returnsan appropriate transformation
See alsoapplyTransform, scaleToFit