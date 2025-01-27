#### setRootItem()


 void TreeView::setRootItem ( TreeViewItem \* newRootItem ) 
 

Sets the item that is displayed in the TreeView.A tree has a single root item which contains as many subitems as it needs. If you want the tree to contain a number of root items, you should still use a single root item above these, but hide it using setRootItemVisible().You can pass nullptr to this method to clear the tree and remove its current root item.The object passed in will not be deleted by the TreeView, it's up to the caller to delete it when no longer needed. BUT make absolutely sure that you don't delete this item until you've removed it from the tree, either by calling setRootItem (nullptr), or by deleting the tree first. You can also use deleteRootItem() as a quick way to delete it.