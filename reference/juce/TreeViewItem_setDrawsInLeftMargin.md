#### setDrawsInLeftMargin()


 void TreeViewItem::setDrawsInLeftMargin ( bool canDrawInLeftMargin ) noexcept 
 

Sets a flag to indicate that the item wants to be allowed to draw all the way across to the left edge of the TreeView.By default this is false, which means that when the paintItem() method is called, its graphics context is clipped to only allow drawing within the item's rectangle. If this flag is set to true, then the graphics context isn't clipped on its left side, so it can draw all the way across to the left margin. Note that the context will still have its origin in the same place though, so the coordinates of anything to its left will be negative. It's mostly useful if you want to draw a wider bar behind the highlighted item.