#### addSubItem()


 void TreeViewItem::addSubItem ( TreeViewItem \* newItem, 
 
 int insertPosition = 1 ) 

Adds a subitem.Parameters

 newItem the object to add to the item's subitem list. Once added, these can be found using getSubItem(). When the items are later removed with removeSubItem() (or when this item is deleted), they will be deleted. 
 
 insertPosition the index which the new item should have when it's added. If this value is less than 0, the item will be added to the end of the list.