#### setCurrentTransactionName()


 void UndoManager::setCurrentTransactionName ( const String & newName ) 
 

Changes the name stored for the current transaction.Each transaction is given a name when the beginNewTransaction() method is called, but this can be used to change that name without starting a new transaction.