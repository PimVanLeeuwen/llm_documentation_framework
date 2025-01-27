#### stopTimer()


 void MultiTimer::stopTimer ( int timerID ) noexcept 
 

Stops a timer.If a timer has been started with the given ID number, it will be cancelled. No more callbacks will be made for the specified timer after this method returns.If this is called from a different thread, any callbacks that may be currently executing may be allowed to finish before the method returns.