#### getNumRows()


 virtual int TableListBoxModel::getNumRows ( ) pure virtual 
 

This must return the number of rows currently in the table.If the number of rows changes, you must call TableListBox::updateContent() to cause it to refresh the list.