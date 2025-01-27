#### itemDragMove()


 virtual void DragAndDropTarget::itemDragMove ( const SourceDetails & dragSourceDetails ) virtual 
 

Callback to indicate that the user is dragging something over this component.This gets called when the user moves the mouse over this component while dragging something. Normally overriding itemDragEnter() and itemDragExit() are enough, but this lets you know what happens inbetween.Parameters

 dragSourceDetails contains information about the source of the drag operation. 
 


Reimplemented in Toolbar, and TreeView.