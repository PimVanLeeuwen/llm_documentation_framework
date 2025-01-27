#### restoreOpennessState()


 void TreeViewItem::restoreOpennessState ( const XmlElement & xml ) 
 

Restores the openness of this item and all its subitems from a saved state.See TreeView::restoreOpennessState for more details.You'd normally want to use TreeView::restoreOpennessState() rather than call it for a specific item, but this can be handy if you need to briefly save the state for a section of the tree.See alsoTreeView::restoreOpennessState, getOpennessState