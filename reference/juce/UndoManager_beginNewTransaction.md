#### beginNewTransaction() [2/2]


 void UndoManager::beginNewTransaction ( const String & actionName ) 
 

Starts a new group of actions that together will be treated as a single transaction.All actions that are passed to the perform() method between calls to this method are grouped together and undone/redone together by a single call to undo() or redo().Parameters

 actionName a description of the transaction that is about to be performed