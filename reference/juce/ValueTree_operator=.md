#### operator=()


 ValueTree & ValueTree::operator= ( const ValueTree & ) 
 

Changes this object to be a reference to the given tree.Note that calling this just points this at the new object and invokes the Listener::valueTreeRedirected callback, but it's not an undoable operation. If you're trying to replace an entire tree in an undoable way, you probably want to use copyPropertiesAndChildrenFrom() instead.