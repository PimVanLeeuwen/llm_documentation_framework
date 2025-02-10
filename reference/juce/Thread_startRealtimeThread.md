#### startRealtimeThread()


 bool Thread::startRealtimeThread ( const RealtimeOptions & options ) 
 

Starts the thread with realtime performance characteristics on platforms that support it.You cannot change the options of a running realtime thread, nor switch a nonrealtime thread to a realtime thread. To make these changes you must first stop the thread and then restart with different options.Parameters

 options Realtime options the thread should be created with. 
 



See alsostartThread, RealtimeOptions