#### postMessage()


 void MessageListener::postMessage ( Message \* message ) const 
 

Sends a message to the message queue, for asynchronous delivery to this listener later on.This method can be called safely by any thread.Parameters

 message the message object to send this will be deleted automatically by the message queue, so make sure it's allocated on the heap, not the stack! 
 



See alsohandleMessage