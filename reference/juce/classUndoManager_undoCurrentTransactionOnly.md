#### undoCurrentTransactionOnly()


 bool UndoManager::undoCurrentTransactionOnly ( ) 
 

Tries to rollback any actions that were added to the current transaction.This will perform an undo() only if there are some actions in the undo list that were added after the last call to beginNewTransaction().This is useful because it lets you call beginNewTransaction(), then perform an operation which may or may not actually perform some actions, and then call this method to get rid of any actions that might have been done without it rolling back the previous transaction if nothing was actually done.Returnstrue if any actions were undone.