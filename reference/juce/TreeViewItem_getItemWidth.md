#### getItemWidth()


 virtual int TreeViewItem::getItemWidth ( ) const virtual 
 

Must return the width required by this item.If your item needs to have a particular width in pixels, return that value; if you'd rather have it just fill whatever space is available in the TreeView, return 1.If all your items return 1, no horizontal scrollbar will be shown, but if any items have fixed widths and extend beyond the width of the TreeView, a scrollbar will appear.Each item can be a different width, but if they change width, you should call treeHasChanged() to update the tree.