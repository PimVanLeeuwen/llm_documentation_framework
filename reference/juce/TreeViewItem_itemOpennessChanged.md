#### itemOpennessChanged()


 virtual void TreeViewItem::itemOpennessChanged ( bool isNowOpen ) virtual 
 

Called when an item is opened or closed.When setOpen() is called and the item has specified that it might have subitems with the mightContainSubItems() method, this method is called to let the item create or manage its subitems.So when this is called with isNowOpen set to true (i.e. when the item is being opened), a subclass might choose to use clearSubItems() and addSubItem() to refresh its subitem list.When this is called with isNowOpen set to false, the subclass might want to use clearSubItems() to save on space, or it might choose to leave them, depending on the nature of the tree.You could also use this callback as a trigger to start a background process which asynchronously creates subitems and adds them, if that's more appropriate for the task in hand.See alsomightContainSubItems