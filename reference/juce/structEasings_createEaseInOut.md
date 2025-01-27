#### createEaseInOut()


 static std::function< float(float)> Easings::createEaseInOut ( ) static 
 

Returns the easing function createCubicBezier (0.42f, 0.0f, 0.58f, 1.0f).This indicates that the interpolation starts slowly, speeds up, and then slows down towards the end. At the beginning, it behaves like createEaseIn(); at the end, it behaves like createEaseOut().This is equivalent to using the "easeinout" keyword when specifying a timingfunction in CSS.See alsocreateCubicBezier, createEase, createEaseIn, createEaseInOut