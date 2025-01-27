#### startTimer()


 void HighResolutionTimer::startTimer ( int intervalInMilliseconds ) 
 

Starts the timer and sets the length of interval required.If the timer has already started, this will reset the timer, so the time between calling this method and the next timer callback will not be less than the interval length passed in.In exceptional circumstances the dedicated timer thread may not start, if this is a potential concern for your use case, you can call isTimerRunning() to confirm if the timer actually started.On Windows the underlying API only allows 16 highresolution timers to run simultaneously in the same process. A fallback timer will be used when this limit is exceeded but the precision may be significantly compromised. This is a particular concern for plugins, because other plugins in the same host process may already have timers running. To avoid issues, try to use the minimum number of HighResolutionTimers possible. For example, consider using a SharedResourcePointer so that all instances of the same plugin running in the same same process can share a single HighResolutionTimer instance.Parameters

 intervalInMilliseconds the interval to use (a value of zero or less will stop the timer)