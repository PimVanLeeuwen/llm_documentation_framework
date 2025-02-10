#### getRowPosition()


 Rectangle< int > ListBox::getRowPosition ( int rowNumber, bool relativeToComponentTopLeft ) const noexcept 
 

Returns the position of one of the rows, relative to the topleft of the listbox.This may be offscreen, and the range of the row number that is passedin is not checked to see if it's a valid row.