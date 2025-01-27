#### createEaseOut()


 static std::function< float(float)> Easings::createEaseOut ( ) static 
 

Returns the easing function createCubicBezier (0.0f, 0.0f, 0.58f, 1.0f).This indicates that the interpolation starts abruptly and then progressively slows down towards the end.This is equivalent to using the "easeout" keyword when specifying a timingfunction in CSS.See alsocreateCubicBezier, createEase, createEaseIn, createEaseInOut, createEaseOutBack