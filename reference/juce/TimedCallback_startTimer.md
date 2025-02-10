#### startTimer()


 void Timer::startTimer ( int intervalInMilliseconds ) noexcept 
 

Starts the timer and sets the length of interval required.If the timer is already started, this will reset it, so the time between calling this method and the next timer callback will not be less than the interval length passed in.Parameters

 intervalInMilliseconds the interval to use (any value less than 1 will be rounded up to 1)