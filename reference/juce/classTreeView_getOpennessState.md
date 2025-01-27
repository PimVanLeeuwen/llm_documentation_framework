#### getOpennessState()


 std::unique\_ptr< XmlElement > TreeView::getOpennessState ( bool alsoIncludeScrollPosition ) const 
 

Saves the current state of open/closed nodes so it can be restored later.This takes a snapshot of which nodes have been explicitly opened or closed, and records it as XML. To identify node objects it uses the TreeViewItem::getUniqueName() method to create named paths. This means that the same state of open/closed nodes can be restored to a completely different instance of the tree, as long as it contains nodes whose unique names are the same.Parameters

 alsoIncludeScrollPosition if this is true, the state will also include information about where the tree has been scrolled to vertically, so this can also be restored 
 



See alsorestoreOpennessState