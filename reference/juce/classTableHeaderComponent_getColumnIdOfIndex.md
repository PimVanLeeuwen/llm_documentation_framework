#### getColumnIdOfIndex()


 int TableHeaderComponent::getColumnIdOfIndex ( int index, 
 
 bool onlyCountVisibleColumns ) const 

Returns the ID of the column at a given index.If onlyCountVisibleColumns is true, this will count the index amongst the visible columns; otherwise it'll count it amongst all the columns, including any hidden ones.If the index is outofrange, it'll return 0.