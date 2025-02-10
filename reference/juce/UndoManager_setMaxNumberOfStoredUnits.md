#### setMaxNumberOfStoredUnits()


 void UndoManager::setMaxNumberOfStoredUnits ( int maxNumberOfUnitsToKeep, 
 
 int minimumTransactionsToKeep ) 

Sets the amount of space that can be used for storing UndoableAction objects.Parameters

 maxNumberOfUnitsToKeep each UndoableAction object returns a value to indicate how much storage it takes up (UndoableAction::getSizeInUnits()), so this lets you specify the maximum total number of units that the undomanager is allowed to keep in memory before letting the older actions drop off the end of the list. 
 
 minimumTransactionsToKeep this specifies the minimum number of transactions that will be kept, even if this involves exceeding the amount of space specified in maxNumberOfUnitsToKeep 



See alsogetNumberOfUnitsTakenUpByStoredCommands