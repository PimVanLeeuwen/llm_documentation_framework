#### signalThreadShouldExit()


 void Thread::signalThreadShouldExit ( ) 
 

Sets a flag to tell the thread it should stop.Calling this means that the threadShouldExit() method will then return true. The thread should be regularly checking this to see whether it should exit.If your thread makes use of wait(), you might want to call notify() after calling this method, to interrupt any waits that might be in progress, and allow it to reach a point where it can exit.See alsothreadShouldExit, waitForThreadToExit