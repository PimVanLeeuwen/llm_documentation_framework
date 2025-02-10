#### isInterestedInDragSource()


 virtual bool TreeViewItem::isInterestedInDragSource ( const DragAndDropTarget::SourceDetails & dragSourceDetails ) virtual 
 

If you want your item to act as a DragAndDropTarget, implement this method and return true.If you implement this method, you'll also need to implement itemDropped() in order to handle the items when they are dropped. To respond to draganddrop of files from external applications, see isInterestedInFileDrag().See alsoDragAndDropTarget::isInterestedInDragSource, itemDropped