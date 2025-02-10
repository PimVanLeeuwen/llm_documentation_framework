#### sendMessageToWorker()


 bool ChildProcessCoordinator::sendMessageToWorker ( const MemoryBlock & ) 
 

Attempts to send a message to the worker process.This returns true if the message was dispatched, but doesn't check that it actually gets delivered at the other end. If successful, the data will emerge in a call to your ChildProcessWorker::handleMessageFromCoordinator().