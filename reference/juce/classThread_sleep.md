#### sleep()


 static void JUCE\_CALLTYPE Thread::sleep ( int milliseconds ) static 
 

Suspends the execution of the current thread until the specified timeout period has elapsed (note that this may not be exact).The timeout period must not be negative and whilst sleeping the thread cannot be woken up so it should only be used for short periods of time and when other methods such as using a WaitableEvent or CriticalSection are not possible.