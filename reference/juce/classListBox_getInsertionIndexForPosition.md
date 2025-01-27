#### getInsertionIndexForPosition()


 int ListBox::getInsertionIndexForPosition ( int x, int y ) const noexcept 
 

Finds a row index that would be the most suitable place to insert a new item for a given position.This is useful when the user is e.g. dragging and dropping onto the listbox, because it lets you easily choose the best position to insert the item that they drop, based on where they drop it.If the position is out of range, this will return 1. If the position is beyond the end of the list, it will return getNumRows() to indicate the end of the list.See alsogetComponentForRowNumber