#### stopDispatchLoop()


 void MessageManager::stopDispatchLoop ( ) 
 

Sends a signal that the dispatch loop should terminate.After this is called, the runDispatchLoop() or runDispatchLoopUntil() methods will be interrupted and will return.See alsorunDispatchLoop