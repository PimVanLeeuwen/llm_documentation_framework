#### setOpen()


 void TreeViewItem::setOpen ( bool shouldBeOpen ) 
 

Opens or closes the item.When opened or closed, the item's itemOpennessChanged() method will be called, and a subclass should use this callback to create and add any subitems that it needs to.Note that if this is called when the item is in its default openness state, and this call would not change whether it's open or closed, then no change will be stored. If you want to explicitly set the openness state to be nondefault then you should use setOpenness instead.See alsosetOpenness, itemOpennessChanged, mightContainSubItems