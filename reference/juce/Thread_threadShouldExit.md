#### threadShouldExit()


 bool Thread::threadShouldExit ( ) const 
 

Checks whether the thread has been told to stop running.Threads need to check this regularly, and if it returns true, they should return from their run() method at the first possible opportunity.See alsosignalThreadShouldExit, currentThreadShouldExit