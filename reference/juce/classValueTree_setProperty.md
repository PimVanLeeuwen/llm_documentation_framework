#### setProperty()


 ValueTree & ValueTree::setProperty ( const Identifier & name, 
 
 const var & newValue, 
 UndoManager \* undoManager ) 

Changes a named property of the tree.The name identifier must not be an empty string. If the undoManager parameter is not nullptr, its UndoManager::perform() method will be used, so that this change can be undone. Be very careful not to mix undoable and nonundoable changes!See alsovar, getProperty, removeProperty 
Returnsa reference to the value tree, so that you can daisychain calls to this method.