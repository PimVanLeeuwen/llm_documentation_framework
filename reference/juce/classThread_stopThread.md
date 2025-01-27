#### stopThread()


 bool Thread::stopThread ( int timeOutMilliseconds ) 
 

Attempts to stop the thread running.This method will cause the threadShouldExit() method to return true and call notify() in case the thread is currently waiting.Hopefully the thread will then respond to this by exiting cleanly, and the stopThread method will wait for a given timeperiod for this to happen.If the thread is stuck and fails to respond after the timeout, it gets forcibly killed, which is a very bad thing to happen, as it could still be holding locks, etc. which are needed by other parts of your program.Parameters

 timeOutMilliseconds The number of milliseconds to wait for the thread to finish before killing it by force. A negative value in here will wait forever. 
 



Returnstrue if the thread was cleanly stopped before the timeout, or false if it had to be killed by force. 
See alsosignalThreadShouldExit, threadShouldExit, waitForThreadToExit, isThreadRunning