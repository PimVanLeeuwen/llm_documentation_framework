#### undo()


 bool UndoManager::undo ( ) 
 

Tries to rollback the last transaction.Returnstrue if the transaction can be undone, and false if it fails, or if there aren't any transactions to undo 
See alsoundoCurrentTransactionOnly