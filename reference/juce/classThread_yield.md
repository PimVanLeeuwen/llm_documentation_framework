#### yield()


 static void JUCE\_CALLTYPE Thread::yield ( ) static 
 

Yields the current thread's CPU timeslot and allows a new thread to run.If there are no other threads of equal or higher priority currently running then this will return immediately and the current thread will continue to run.