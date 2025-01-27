#### createEaseOutBack()


 static std::function< float(float)> Easings::createEaseOutBack ( ) static 
 

Returns the easing function createCubicBezier (0.34f, 1.56f, 0.64f, 1.0f).This indicates that the interpolation starts abruptly, quickly decelerating before overshooting the target value by approximately 10% and changing direction to slowly head back towards the target value.Like createSpring() this will overshoot causing it to return float values exceeding 1.0f.This is equivalent to easeOutBack as specified on https://easings.net/#easeOutBack.See alsocreateCubicBezier, createEaseOutBack, createSpring