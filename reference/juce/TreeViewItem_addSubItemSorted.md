#### addSubItemSorted()


template<class ElementComparator > 

 void TreeViewItem::addSubItemSorted ( ElementComparator & comparator, 
 
 TreeViewItem \* newItem ) 

Adds a subitem with a sortcomparator, assuming that the existing items are already sorted.Parameters

 comparator the comparator object for sorting see sortSubItems() for details about the methods this class must provide. 
 
 newItem the object to add to the item's subitem list. Once added, these can be found using getSubItem(). When the items are later removed with removeSubItem() (or when this item is deleted), they will be deleted.