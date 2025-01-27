#### getUndoDescriptions()


 StringArray UndoManager::getUndoDescriptions ( ) const 
 

Returns the names of the sequence of transactions that will be performed if undo() is repeatedly called.Note that for transactions where no name was provided, the corresponding string will be empty.See alsoundo, canUndo, getUndoDescription