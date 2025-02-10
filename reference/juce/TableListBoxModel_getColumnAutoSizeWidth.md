#### getColumnAutoSizeWidth()


 virtual int TableListBoxModel::getColumnAutoSizeWidth ( int columnId ) virtual 
 

Returns the best width for one of the columns.If you implement this method, you should measure the width of all the items in this column, and return the best size.Returning 0 means that the column shouldn't be changed.This is used by TableListBox::autoSizeColumn() and TableListBox::autoSizeAllColumns().