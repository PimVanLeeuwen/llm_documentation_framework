#### findItemFromIdentifierString()


 TreeViewItem \* TreeView::findItemFromIdentifierString ( const String & identifierString ) const 
 

Searches the tree for an item with the specified identifier.The identifier string must have been created by calling TreeViewItem::getItemIdentifierString(). If no such item exists, this will return false. If the item is found, all of its items will be automatically opened.