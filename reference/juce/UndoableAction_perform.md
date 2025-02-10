#### perform()


 virtual bool UndoableAction::perform ( ) pure virtual 
 

Overridden by a subclass to perform the action.This method is called by the UndoManager, and shouldn't be used directly by applications.Be careful not to make any calls in a perform() method that could call recursively back into the UndoManager::perform() methodReturnstrue if the action could be performed. 
See alsoUndoManager::perform