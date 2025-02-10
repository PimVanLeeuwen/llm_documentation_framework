#### nudge()


template<typename Behaviour > 

 void AnimatedPosition< Behaviour >::nudge ( double deltaFromCurrentPosition ) 
 

Called outside of a drag operation to cause a nudge in the specified direction.This is intended for use by e.g. mousewheel events.References Timer::startTimerHz().