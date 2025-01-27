#### getThreadId()


 ThreadID Thread::getThreadId ( ) const noexcept 
 

Returns the ID of this thread.That means the ID of this thread object not of the thread that's calling the method. This can change when the thread is started and stopped, and will be invalid if the thread's not actually running.See alsogetCurrentThreadId