#### itemDragExit()


 void Toolbar::itemDragExit ( const SourceDetails & dragSourceDetails ) overridevirtual 
 

Callback to indicate that something has been dragged off the edge of this component.This gets called when the user moves the mouse out of this component while dragging something.If you've used itemDragEnter() to repaint your component and give feedback, use this as a signal to repaint it in its normal state.Parameters

 dragSourceDetails contains information about the source of the drag operation. 
 



See alsoitemDragEnter Reimplemented from DragAndDropTarget.