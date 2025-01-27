#### getDragSourceDescription()


 virtual var TableListBoxModel::getDragSourceDescription ( const SparseSet< int > & currentlySelectedRows ) virtual 
 

To allow rows from your table to be draggedanddropped, implement this method.If this returns a nonnull variant then when the user drags a row, the table will try to find a DragAndDropContainer in its parent hierarchy, and will use it to trigger a draganddrop operation, using this string as the source description, and the listbox itself as the source component.See alsogetDragSourceCustomData, DragAndDropContainer::startDragging