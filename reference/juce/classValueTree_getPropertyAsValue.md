#### getPropertyAsValue()


 Value ValueTree::getPropertyAsValue ( const Identifier & name, 
 
 UndoManager \* undoManager, 
 bool shouldUpdateSynchronously = false ) 

Returns a Value object that can be used to control and respond to one of the tree's properties.The Value object will maintain a reference to this tree, and will use the undo manager when it needs to change the value. Attaching a Value::Listener to the value object will provide callbacks whenever the property changes. If shouldUpdateSynchronously is true the Value::Listener will be updated synchronously.See alsoValueSource::sendChangeMessage (bool)