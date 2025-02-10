#### stopTimer()


 void HighResolutionTimer::stopTimer ( ) 
 

Stops the timer.This method may block while it waits for pending callbacks to complete. Once it returns, no more callbacks will be made. If it is called from the timer's own thread, it will cancel the timer after the current callback returns.To prevent data races it's normally best practice to call this in the derived classes destructor, even if stopTimer() was called in the hiResTimerCallback().