#### shouldDrawDragImageWhenOver()


 virtual bool DragAndDropTarget::shouldDrawDragImageWhenOver ( ) virtual 
 

Overriding this allows the target to tell the drag container whether to draw the drag image while the cursor is over it.By default it returns true, but if you return false, then the normal drag image will not be shown when the cursor is over this target.