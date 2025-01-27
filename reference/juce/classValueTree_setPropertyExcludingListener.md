#### setPropertyExcludingListener()


 ValueTree & ValueTree::setPropertyExcludingListener ( Listener \* listenerToExclude, 
 
 const Identifier & name, 
 const var & newValue, 
 UndoManager \* undoManager ) 

Changes a named property of the tree, but will not notify a specified listener of the change.See alsosetProperty