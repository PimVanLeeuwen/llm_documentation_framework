#### isInterestedInDragSource()


 bool TreeView::isInterestedInDragSource ( const SourceDetails & dragSourceDetails ) overridevirtual 
 

Callback to check whether this target is interested in the type of object being dragged.Parameters

 dragSourceDetails contains information about the source of the drag operation. 
 



Returnstrue if this component wants to receive the other callbacks regarding this type of object; if it returns false, no other callbacks will be made. Implements DragAndDropTarget.