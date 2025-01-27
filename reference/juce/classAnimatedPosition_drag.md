#### drag()


template<typename Behaviour > 

 void AnimatedPosition< Behaviour >::drag ( double deltaFromStartOfDrag ) 
 

Called during a mousedrag operation, to indicate that the mouse has moved.The delta is the difference between the position when beginDrag() was called and the new position that's required.