#### dispatchPendingMessages()


 void ChangeBroadcaster::dispatchPendingMessages ( ) 
 

If a change message has been sent but not yet dispatched, this will call sendSynchronousChangeMessage() to make the callback immediately.For threadsafety reasons, you must only call this method on the main message thread.