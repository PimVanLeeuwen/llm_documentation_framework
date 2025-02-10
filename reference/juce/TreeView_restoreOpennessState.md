#### restoreOpennessState()


 void TreeView::restoreOpennessState ( const XmlElement & newState, 
 
 bool restoreStoredSelection ) 

Restores a previously saved arrangement of open/closed nodes.This will try to restore a snapshot of the tree's state that was created by the getOpennessState() method. If any of the nodes named in the original XML aren't present in this tree, they will be ignored.If restoreStoredSelection is true, it will also try to reselect any items that were selected in the stored state.See alsogetOpennessState