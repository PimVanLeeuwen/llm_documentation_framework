#### getOpennessState()


 std::unique\_ptr< XmlElement > TreeViewItem::getOpennessState ( ) const 
 

Saves the current state of open/closed nodes so it can be restored later.This takes a snapshot of which subnodes have been explicitly opened or closed, and records it as XML. To identify node objects it uses the TreeViewItem::getUniqueName() method to create named paths. This means that the same state of open/closed nodes can be restored to a completely different instance of the tree, as long as it contains nodes whose unique names are the same.You'd normally want to use TreeView::getOpennessState() rather than call it for a specific item, but this can be handy if you need to briefly save the state for a section of the tree.Note that if all nodes of the tree are in their default state, then this may return a nullptr.See alsoTreeView::getOpennessState, restoreOpennessState