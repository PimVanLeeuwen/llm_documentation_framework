#### getCurrentThreadId()


 static ThreadID JUCE\_CALLTYPE Thread::getCurrentThreadId ( ) static 
 

Returns an id that identifies the caller thread.To find the ID of a particular thread object, use getThreadId().Returnsa unique identifier that identifies the calling thread. 
See alsogetThreadId Referenced by ThreadLocalValue< Type >::get(), and ThreadLocalValue< Type >::releaseCurrentThreadStorage().