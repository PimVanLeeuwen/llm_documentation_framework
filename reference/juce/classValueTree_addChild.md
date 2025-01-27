#### addChild()


 void ValueTree::addChild ( const ValueTree & child, 
 
 int index, 
 UndoManager \* undoManager ) 

Adds a child to this tree.Make sure that the child being added has first been removed from any former parent before calling this, or else you'll hit an assertion. If the index is < 0 or greater than the current number of subtrees, the new one will be added at the end of the list. If the undoManager parameter is not nullptr, its UndoManager::perform() method will be used, so that this change can be undone. Be very careful not to mix undoable and nonundoable changes!See alsoappendChild, removeChild