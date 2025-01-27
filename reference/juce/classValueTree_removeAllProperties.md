#### removeAllProperties()


 void ValueTree::removeAllProperties ( UndoManager \* undoManager ) 
 

Removes all properties from the tree.If the undoManager parameter is not nullptr, its UndoManager::perform() method will be used, so that this change can be undone. Be very careful not to mix undoable and nonundoable changes!