#### createSolidAreaMask()


 void Image::createSolidAreaMask ( RectangleList< int > & result, 
 
 float alphaThreshold ) const 

Creates a RectangleList containing rectangles for all nontransparent pixels of the image.Parameters

 result the list that will have the area added to it 
 
 alphaThreshold for a semitransparent image, any pixels whose alpha is above this level will be considered opaque