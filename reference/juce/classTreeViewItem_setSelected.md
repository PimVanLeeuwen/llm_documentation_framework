#### setSelected()


 void TreeViewItem::setSelected ( bool shouldBeSelected, 
 
 bool deselectOtherItemsFirst, 
 NotificationType shouldNotify = sendNotification ) 

Selects or deselects the item.If shouldNotify == sendNotification, then a callback will be made to itemSelectionChanged() if the item's selection has changed.