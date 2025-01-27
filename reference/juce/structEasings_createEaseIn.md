#### createEaseIn()


 static std::function< float(float)> Easings::createEaseIn ( ) static 
 

Returns the easing function createCubicBezier (0.42f, 0.0f, 1.0f, 1.0f).This indicates that the interpolation starts slowly, then progressively speeds up until the end, at which point it stops abruptly.This is equivalent to using the "easein" keyword when specifying a timingfunction in CSS.See alsocreateCubicBezier, createEase, createEaseOut, createEaseInOut