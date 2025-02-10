#### setAffinityMask()


 void Thread::setAffinityMask ( uint32 affinityMask ) 
 

Sets the affinity mask for the thread.This will only have an effect next time the thread is started i.e. if the thread is already running when called, it'll have no effect.See alsosetCurrentThreadAffinityMask