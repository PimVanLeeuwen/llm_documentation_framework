#### getIndexOfColumnId()


 int TableHeaderComponent::getIndexOfColumnId ( int columnId, 
 
 bool onlyCountVisibleColumns ) const 

Returns the index of a given column.If there's no such column ID, this will return 1.If onlyCountVisibleColumns is true, this will return the index amongst the visible columns; otherwise it'll return the index amongst all the columns, including any hidden ones.