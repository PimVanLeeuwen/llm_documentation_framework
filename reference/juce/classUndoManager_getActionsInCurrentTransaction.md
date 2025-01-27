#### getActionsInCurrentTransaction()


 void UndoManager::getActionsInCurrentTransaction ( Array< const UndoableAction \* > & actionsFound ) const 
 

Returns a list of the UndoableAction objects that have been performed during the transaction that is currently open.Effectively, this is the list of actions that would be undone if undoCurrentTransactionOnly() were to be called now.The first item in the list is the earliest action performed.