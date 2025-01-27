#### getSelectedRow()


 int ListBox::getSelectedRow ( int index = 0 ) const 
 

Returns the row number of a selected row.This will return the row number of the Nth selected row. The row numbers returned will be sorted in order from low to high.Parameters

 index the index of the selected row to return, (from 0 to getNumSelectedRows() 1) 
 



Returnsthe row number, or 1 if the index was out of range or if there aren't any rows selected 
See alsogetNumSelectedRows, isRowSelected, getLastRowSelected