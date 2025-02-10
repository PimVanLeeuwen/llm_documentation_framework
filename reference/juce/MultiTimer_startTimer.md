#### startTimer()


 void MultiTimer::startTimer ( int timerID, int intervalInMilliseconds ) noexcept 
 

Starts a timer and sets the length of interval required.If the timer is already started, this will reset it, so the time between calling this method and the next timer callback will not be less than the interval length passed in.Parameters

 timerID a unique Id number that identifies the timer to start. This is the id that will be passed back to the timerCallback() method when this timer is triggered 
 
 intervalInMilliseconds the interval to use (any values less than 1 will be rounded up to 1)