#### handleConnectionLost()


 virtual void ChildProcessWorker::handleConnectionLost ( ) virtual 
 

This will be called when the connection to the coordinator process is lost.The call may be made from any thread (including the message thread). Typically, if your process only exists to act as a worker, you should probably exit when this happens.