#### setPosition()


template<typename Behaviour > 

 void AnimatedPosition< Behaviour >::setPosition ( double newPosition ) 
 

Explicitly sets the position and stops any further movement.This will cause a synchronous call to any listeners if the position actually changes.References Timer::stopTimer().