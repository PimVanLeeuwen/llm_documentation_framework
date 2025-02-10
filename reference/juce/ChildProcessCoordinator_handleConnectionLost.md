#### handleConnectionLost()


 virtual void ChildProcessCoordinator::handleConnectionLost ( ) virtual 
 

This will be called when the worker process dies or is somehow disconnected.The call will probably be made on a background thread, so be careful with your threadsafety!