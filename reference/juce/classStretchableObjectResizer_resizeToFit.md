#### resizeToFit()


 void StretchableObjectResizer::resizeToFit ( double targetSize ) 
 

Resizes all the items to fit this amount of space.This will attempt to fit them in without exceeding each item's minimum and maximum sizes. In cases where none of the items can be expanded or enlarged any further, the final size may be greater or less than the size passed in.After calling this method, you can retrieve the new sizes with the getItemSize() method.