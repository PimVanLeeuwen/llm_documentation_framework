#### scaleToFit()


 void Path::scaleToFit ( float x, float y, float width, float height, bool preserveProportions ) noexcept 
 

Rescales this path to make it fit neatly into a given space.This is effectively a quick way of calling applyTransform (getTransformToScaleToFit (x, y, w, h, preserveProportions))Parameters

 x the x position of the rectangle to fit the path inside 
 
 y the y position of the rectangle to fit the path inside 
 width the width of the rectangle to fit the path inside 
 height the height of the rectangle to fit the path inside 
 preserveProportions if true, it will fit the path into the space without altering its horizontal/vertical scale ratio; if false, it will distort the path to fill the specified ratio both horizontally and vertically 



See alsoapplyTransform, getTransformToScaleToFit