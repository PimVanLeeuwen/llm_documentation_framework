#### addChildProcessExitedListener()


 auto ChildProcessManager::addChildProcessExitedListener ( std::function< void(ChildProcess \*)> listener ) 
 

Registers a callback function that is called for every ChildProcess that terminated.This registration is deleted when the returned ErasedScopedGuard is deleted.