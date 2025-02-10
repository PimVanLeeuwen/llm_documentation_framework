#### handleMessageFromWorker()


 virtual void ChildProcessCoordinator::handleMessageFromWorker ( const MemoryBlock & ) virtual 
 

This will be called to deliver a message from the worker process.The call will probably be made on a background thread, so be careful with your threadsafety!