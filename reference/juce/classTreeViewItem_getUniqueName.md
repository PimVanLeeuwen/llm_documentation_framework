#### getUniqueName()


 virtual String TreeViewItem::getUniqueName ( ) const virtual 
 

Returns a string to uniquely identify this item.If you're planning on using the TreeView::getOpennessState() method, then these strings will be used to identify which nodes are open. The string should be unique amongst the item's sibling items, but it's ok for there to be duplicates at other levels of the tree.If you're not going to store the state, then it's ok not to bother implementing this method.