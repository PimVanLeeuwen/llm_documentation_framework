#### getPriority()


 Priority Thread::getPriority ( ) const protected 
 

Returns the current priority of this thread.This can only be called from the target thread. Doing so from another thread will cause an assert.See alsosetPriority