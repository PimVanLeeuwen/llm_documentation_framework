#### perform() [2/2]


 bool UndoManager::perform ( UndoableAction \* action, 
 
 const String & actionName ) 

Performs an action and also gives it a name.Parameters

 action the action to perform this object will be deleted by the UndoManager when no longer needed 
 
 actionName if this string is nonempty, the current transaction will be given this name; if it's empty, the current transaction name will be left unchanged. See setCurrentTransactionName() 



Returnstrue if the command succeeds see UndoableAction::perform 
See alsobeginNewTransaction