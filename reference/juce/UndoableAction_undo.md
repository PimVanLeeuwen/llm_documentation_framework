#### undo()


 virtual bool UndoableAction::undo ( ) pure virtual 
 

Overridden by a subclass to undo the action.This method is called by the UndoManager, and shouldn't be used directly by applications.Be careful not to make any calls in an undo() method that could call recursively back into the UndoManager::perform() methodReturnstrue if the action could be undone without any errors. 
See alsoUndoManager::perform