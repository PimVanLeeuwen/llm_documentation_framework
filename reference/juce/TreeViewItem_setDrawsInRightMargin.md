#### setDrawsInRightMargin()


 void TreeViewItem::setDrawsInRightMargin ( bool canDrawInRightMargin ) noexcept 
 

Sets a flag to indicate that the item wants to be allowed to draw all the way across to the right edge of the TreeView.Similar to setDrawsInLeftMargin: when this flag is set to true, then the graphics context isn't clipped on the right side. Unlike setDrawsInLeftMargin, you will very rarely need to use this function, as this method won't clip the right margin unless your TreeViewItem overrides getItemWidth to return a positive value.See alsosetDrawsInLeftMargin, getItemWidth