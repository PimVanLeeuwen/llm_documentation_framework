#### releaseCurrentThreadStorage()


template<typename Type > 

 void ThreadLocalValue< Type >::releaseCurrentThreadStorage ( ) 
 

Called by a thread before it terminates, to allow this class to release any storage associated with the thread.References Atomic< Type >::get(), and Thread::getCurrentThreadId().