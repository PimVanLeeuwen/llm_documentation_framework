#### removeChild() [2/2]


 void ValueTree::removeChild ( int childIndex, 
 
 UndoManager \* undoManager ) 

Removes a subtree from this tree.If the index is outofrange, nothing will be changed. If the undoManager parameter is not nullptr, its UndoManager::perform() method will be used, so that this change can be undone. Be very careful not to mix undoable and nonundoable changes!