#### runDispatchLoopUntil()


 bool MessageManager::runDispatchLoopUntil ( int millisecondsToRunFor ) 
 

Synchronously dispatches messages until a given time has elapsed.Returns false if a quit message has been posted by a call to stopDispatchLoop(), otherwise returns true.