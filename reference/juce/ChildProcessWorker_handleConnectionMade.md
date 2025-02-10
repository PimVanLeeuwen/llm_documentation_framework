#### handleConnectionMade()


 virtual void ChildProcessWorker::handleConnectionMade ( ) virtual 
 

This will be called when the coordinator process finishes connecting to this worker.The call will probably be made on a background thread, so be careful with your threadsafety!