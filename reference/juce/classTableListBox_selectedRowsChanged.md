#### selectedRowsChanged()


 void TableListBox::selectedRowsChanged ( int lastRowSelected ) overridevirtual 
 

Override this to be informed when rows are selected or deselected.This will be called whenever a row is selected or deselected. If a range of rows is selected all at once, this will just be called once for that event.Parameters

 lastRowSelected the last row that the user selected. If no rows are currently selected, this may be 1. 
 


Reimplemented from ListBoxModel.