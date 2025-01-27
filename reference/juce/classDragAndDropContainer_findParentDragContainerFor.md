#### findParentDragContainerFor()


 static DragAndDropContainer \* DragAndDropContainer::findParentDragContainerFor ( Component \* childComponent ) static 
 

Utility to find the DragAndDropContainer for a given Component.This will search up this component's parent hierarchy looking for the first parent component which is a DragAndDropContainer.It's useful when a component wants to call startDragging but doesn't know the DragAndDropContainer it should to use.Obviously this may return nullptr if it doesn't find a suitable component.