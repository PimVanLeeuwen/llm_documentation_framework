#### hiResTimerCallback()


 virtual void HighResolutionTimer::hiResTimerCallback ( ) pure virtual 
 

The userdefined callback routine that actually gets called periodically.This will be called on a dedicated timer thread, so make sure your implementation is threadsafe!On some platforms the dedicated timer thread may be shared with other HighResolutionTimer's so aim to complete any work in this callback as fast as possible.It's perfectly ok to call startTimer() or stopTimer() from within this callback to change the subsequent intervals. However, if you call stopTimer() in the callback it's still best practice to call stopTimer() from the destructor in order to avoid data races.