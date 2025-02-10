#### withOnCompleteCallback()


 ValueAnimatorBuilder ValueAnimatorBuilder::withOnCompleteCallback ( std::function< void()> value ) const nodiscard 
 

Use this function to optionally specify an on complete callback.This function will be called after the Animator reached a progress value >= 1.0, or in the case of an infinitely running animation, if Animator::complete() has been called.