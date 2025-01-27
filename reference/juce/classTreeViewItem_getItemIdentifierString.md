#### getItemIdentifierString()


 String TreeViewItem::getItemIdentifierString ( ) const 
 

Creates a string that can be used to uniquely retrieve this item in the tree.The string that is returned can be passed to TreeView::findItemFromIdentifierString(). The string takes the form of a path, constructed from the getUniqueName() of this item and all its parents, so these must all be correctly implemented for it to work.See alsoTreeView::findItemFromIdentifierString, getUniqueName