#### stopTimer()


 void Timer::stopTimer ( ) noexcept 
 

Stops the timer.No more timer callbacks will be triggered after this method returns.Note that if you call this from a background thread while the messagethread is already in the middle of your callback, then this method will cancel any future timer callbacks, but it will return without waiting for the current one to finish. The current callback will continue, possibly still running some of your timer code after this method has returned.Referenced by ~TimedCallback().