#### createBounce()


 static std::function< float(float)> Easings::createBounce ( int numBounces = 3 ) static 
 

Returns an easing function that behaves like a bouncy ball dropped on the ground.The function will bounce numBounces times on the input range of [0, 1] before coming to stop, each bounce is less pronounced than the previous.This is equivalent to easeInOutCubic as specified on https://easings.net/#easeOutBounce.