#### getRedoDescriptions()


 StringArray UndoManager::getRedoDescriptions ( ) const 
 

Returns the names of the sequence of transactions that will be performed if redo() is repeatedly called.Note that for transactions where no name was provided, the corresponding string will be empty.See alsoredo, canRedo, getRedoDescription