#### getItemHeight()


 virtual int TreeViewItem::getItemHeight ( ) const virtual 
 

Must return the height required by this item.This is the height in pixels that the item will take up. Items in the tree can be different heights, but if they change height, you should call treeHasChanged() to update the tree.