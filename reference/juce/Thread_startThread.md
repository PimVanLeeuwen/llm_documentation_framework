#### startThread() [2/2]


 bool Thread::startThread ( Priority newPriority ) 
 

Attempts to start a new thread with a given priority.This will cause the thread's run() method to be called by a new thread. If this thread is already running, startThread() won't do anything.If a thread cannot be created with the requested priority, this will return false and Thread::run() will not be called. An exception to this is the Android platform, which always starts a thread and attempts to upgrade the thread after creation.Parameters

 newPriority Priority the thread should be assigned. This parameter is ignored on Linux. 
 



Returnstrue if the thread started successfully, false if it was unsuccesful.
See alsostartThread, setPriority, startRealtimeThread