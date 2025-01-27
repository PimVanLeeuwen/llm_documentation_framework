#### isComplete()


 bool Animator::isComplete ( ) const 
 

Returns true if the Animator has reached the point of completion either because complete() has been called on it, or in case of the ValueAnimator, if it reached a progress of >= 1.0.You typically don't need to call this function, because in any case a completed Animator will receive an update callback with a progress value of 1.0 and following that the on complete callback will be called.