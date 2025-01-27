#### getDragSourceDescription()


 virtual var TreeViewItem::getDragSourceDescription ( ) virtual 
 

To allow items from your TreeView to be draggedanddropped, implement this method.If this returns a nonnull variant then when the user drags an item, the TreeView will try to find a DragAndDropContainer in its parent hierarchy, and will use it to trigger a draganddrop operation, using this string as the source description, with the TreeView itself as the source component.If you need more complex draganddrop behaviour, you can use custom components for the items, and use those to trigger the drag.To accept draganddrop in your tree, see isInterestedInDragSource(), isInterestedInFileDrag(), etc.See alsoDragAndDropContainer::startDragging