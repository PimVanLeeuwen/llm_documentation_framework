#### itemDropped()


 virtual void TreeViewItem::itemDropped ( const DragAndDropTarget::SourceDetails & dragSourceDetails, int insertIndex ) virtual 
 

When a things are dropped into this item, this callback is invoked.For this to work, you need to have also implemented isInterestedInDragSource(). The insertIndex value indicates where in the list of subitems the new items should be placed. If files are dropped onto an area of the tree where there are no visible items, this method is called on the root item of the tree, with an insert index of 0.See alsoisInterestedInDragSource, DragAndDropTarget::itemDropped