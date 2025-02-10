#### createAndStartManagedChildProcess()


template<typename... Args> 

 std::shared\_ptr< ChildProcess > ChildProcessManager::createAndStartManagedChildProcess ( Args &&... args ) 
 

Creates a new ChildProcess and starts it with the provided arguments.The arguments are the same as the overloads to ChildProcess::start().The manager will keep the returned ChildProcess object alive until it terminates and its return value has been queried. Calling ChildProcess::kill() on the returned object will eventually cause its removal from the ChildProcessManager after it terminates.