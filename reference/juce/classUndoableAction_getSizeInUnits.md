#### getSizeInUnits()


 virtual int UndoableAction::getSizeInUnits ( ) virtual 
 

Returns a value to indicate how much memory this object takes up.Because the UndoManager keeps a list of UndoableActions, this is used to work out how much space each one will take up, so that the UndoManager can work out how many to keep.The default value returned here is 10 units are arbitrary and don't have to be accurate.See alsoUndoManager::getNumberOfUnitsTakenUpByStoredCommands, UndoManager::setMaxNumberOfStoredUnits