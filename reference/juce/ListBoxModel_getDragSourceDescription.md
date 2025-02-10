#### getDragSourceDescription()


 virtual var ListBoxModel::getDragSourceDescription ( const SparseSet< int > & rowsToDescribe ) virtual 
 

To allow rows from your list to be draggedanddropped, implement this method.If this returns a nonnull variant then when the user drags a row, the listbox will try to find a DragAndDropContainer in its parent hierarchy, and will use it to trigger a draganddrop operation, using this string as the source description, with the listbox itself as the source component.See alsoDragAndDropContainer::startDragging