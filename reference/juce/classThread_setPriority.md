#### setPriority()


 bool Thread::setPriority ( Priority newPriority ) protected 
 

Attempts to set the priority for this thread.Returns true if the new priority was set successfully, false if not.This can only be called from the target thread. Doing so from another thread will cause an assert.Parameters

 newPriority The new priority to be applied to the thread. Note: This has no effect on Linux platforms, subsequent calls to 'getPriority' will return this value. 
 



See alsoPriority 

Member Data Documentation