#### runDispatchLoop()


 void MessageManager::runDispatchLoop ( ) 
 

Runs the event dispatch loop until a stop message is posted.This method is only intended to be run by the application's startup routine, as it blocks, and will only return after the stopDispatchLoop() method has been used.See alsostopDispatchLoop