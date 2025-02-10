#### getItemPosition()


 Rectangle< int > TreeViewItem::getItemPosition ( bool relativeToTreeViewTopLeft ) const noexcept 
 

Returns the rectangle that this item occupies.If relativeToTreeViewTopLeft is true, the coordinates are relative to the topleft of the TreeView comp, so this will depend on the scrollposition of the tree. If false, it is relative to the topleft of the topmost item in the tree (so this would be unaffected by scrolling the view).