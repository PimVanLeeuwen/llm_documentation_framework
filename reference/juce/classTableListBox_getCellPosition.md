#### getCellPosition()


 Rectangle< int > TableListBox::getCellPosition ( int columnId, 
 
 int rowNumber, 
 bool relativeToComponentTopLeft ) const 

Returns the position of one of the cells in the table.If relativeToComponentTopLeft is true, the coordinates are relative to the table component's topleft. The row number isn't checked to see if it's inrange, but the column ID must exist or this will return an empty rectangle.If relativeToComponentTopLeft is false, the coordinates are relative to the topleft of the table's topleft cell.