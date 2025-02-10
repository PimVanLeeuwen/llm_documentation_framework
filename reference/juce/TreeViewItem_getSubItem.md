#### getSubItem()


 TreeViewItem \* TreeViewItem::getSubItem ( int index ) const noexcept 
 

Returns one of the item's subitems.Remember that the object returned might get deleted at any time when its parent item is closed or refreshed, depending on the nature of the items you're using.See alsogetNumSubItems