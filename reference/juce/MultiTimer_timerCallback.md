#### timerCallback()


 virtual void MultiTimer::timerCallback ( int timerID ) pure virtual 
 

The userdefined callback routine that actually gets called by each of the timers that are running.It's perfectly ok to call startTimer() or stopTimer() from within this callback to change the subsequent intervals.