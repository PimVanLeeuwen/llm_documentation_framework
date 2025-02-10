#### callFunctionOnMessageThread()


 void \* MessageManager::callFunctionOnMessageThread ( MessageCallbackFunction \* callback, 
 
 void \* userData ) 

Calls a function using the messagethread.This can be used by any thread to cause this function to be calledback by the message thread. If it's the messagethread that's calling this method, then the function will just be called; if another thread is calling, a message will be posted to the queue, and this method will block until that message is delivered, the function is called, and the result is returned.Be careful not to cause any deadlocks with this! It's easy to do e.g. if the caller thread has a critical section locked, which an unrelated message callback then tries to lock before the message thread gets round to processing this callback.Parameters

 callback the function to call its signature must be void\* myCallbackFunction (void\*) 
 
 userData a userdefined pointer that will be passed to the function that gets called 



Returnsthe value that the callback function returns. 
See alsoMessageManagerLock