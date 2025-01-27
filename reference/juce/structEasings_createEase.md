#### createEase()


 static std::function< float(float)> Easings::createEase ( ) static 
 

Returns the easing function createCubicBezier (0.25f, 0.1f, 0.25f, 1.0f).This indicates that the interpolation starts slowly, accelerates sharply, and then slows gradually towards the end. It is similar to createEaseInOut(), though it accelerates more sharply at the beginning.This is equivalent to using the "ease" keyword when specifying a timingfunction in CSS.This is the default easing used by the ValueAnimatorBuilder class if no other easing function is specified.See alsocreateCubicBezier, createEaseIn, createEaseOut, createEaseInOut