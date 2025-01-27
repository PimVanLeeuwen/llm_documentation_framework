#### currentThreadShouldExit()


 static bool Thread::currentThreadShouldExit ( ) static 
 

Checks whether the current thread has been told to stop running.On the message thread, this will always return false, otherwise it will return threadShouldExit() called on the current thread.See alsothreadShouldExit