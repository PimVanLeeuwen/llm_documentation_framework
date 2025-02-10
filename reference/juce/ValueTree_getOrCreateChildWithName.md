#### getOrCreateChildWithName()


 ValueTree ValueTree::getOrCreateChildWithName ( const Identifier & type, 
 
 UndoManager \* undoManager ) 

Returns the first subtree with the specified type name, creating and adding a child with this name if there wasn't already one there.The only time this will return an invalid object is when the object that you're calling the method on is itself invalid.See alsogetChildWithName