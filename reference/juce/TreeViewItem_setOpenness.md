#### setOpenness()


 void TreeViewItem::setOpenness ( Openness newOpenness ) 
 

Opens or closes the item.If this causes the value of isOpen() to change, then the item's itemOpennessChanged() method will be called, and a subclass should use this callback to create and add any subitems that it needs to.See alsosetOpen