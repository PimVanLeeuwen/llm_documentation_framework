#### sendMessageToCoordinator()


 bool ChildProcessWorker::sendMessageToCoordinator ( const MemoryBlock & ) 
 

Tries to send a message to the coordinator process.This returns true if the message was sent, but doesn't check that it actually gets delivered at the other end. If successful, the data will emerge in a call to your ChildProcessCoordinator::handleMessageFromWorker().