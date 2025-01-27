#### setCurrentThreadAffinityMask()


 static void JUCE\_CALLTYPE Thread::setCurrentThreadAffinityMask ( uint32 affinityMask ) static 
 

Changes the affinity mask for the caller thread.This will change the affinity mask for the thread that calls this static method.See alsosetAffinityMask