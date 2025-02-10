#### handleMessageFromCoordinator()


 virtual void ChildProcessWorker::handleMessageFromCoordinator ( const MemoryBlock & mb ) virtual 
 

This will be called to deliver messages from the coordinator process.The call will probably be made on a background thread, so be careful with your threadsafety! You may want to respond by sending back a message with sendMessageToCoordinator()