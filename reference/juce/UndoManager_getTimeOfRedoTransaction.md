#### getTimeOfRedoTransaction()


 Time UndoManager::getTimeOfRedoTransaction ( ) const 
 

Returns the time to which the state would be restored if redo() was to be called.If a redo isn't currently possible, it'll return Time::getCurrentTime().See alsoredo, canRedo