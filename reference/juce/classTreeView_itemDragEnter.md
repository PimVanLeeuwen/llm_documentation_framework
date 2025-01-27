#### itemDragEnter()


 void TreeView::itemDragEnter ( const SourceDetails & dragSourceDetails ) overridevirtual 
 

Callback to indicate that something is being dragged over this component.This gets called when the user moves the mouse into this component while dragging something.Use this callback as a trigger to make your component repaint itself to give the user feedback about whether the item can be dropped here or not.Parameters

 dragSourceDetails contains information about the source of the drag operation. 
 



See alsoitemDragExit Reimplemented from DragAndDropTarget.