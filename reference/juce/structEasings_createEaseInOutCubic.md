#### createEaseInOutCubic()


 static std::function< float(float)> Easings::createEaseInOutCubic ( ) static 
 

Returns the easing function createCubicBezier (0.65f, 0.0f, 0.35f, 1.0f).This indicates that the interpolation starts slowly, speeds up, and then slows down towards the end. It behaves similar to createEaseInOut() but is more exaggerated and has a more symmetrical curve.This is equivalent to easeInOutCubic as specified on https://easings.net/#easeInOutCubic.See alsocreateCubicBezier, createEaseInOut