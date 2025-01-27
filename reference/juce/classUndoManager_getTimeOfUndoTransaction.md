#### getTimeOfUndoTransaction()


 Time UndoManager::getTimeOfUndoTransaction ( ) const 
 

Returns the time to which the state would be restored if undo() was to be called.If an undo isn't currently possible, it'll return Time().