#### beginDrag()


template<typename Behaviour > 

 void AnimatedPosition< Behaviour >::beginDrag ( ) 
 

Called to indicate that the object is now being controlled by a mousedrag or similar operation.After calling this method, you should make calls to the drag() method each time the mouse drags the position around, and always be sure to finish with a call to endDrag() when the mouse is released, which allows the position to continue moving freely according to the specified behaviour.References Timer::stopTimer().