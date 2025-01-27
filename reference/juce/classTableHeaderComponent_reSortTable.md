#### reSortTable()


 void TableHeaderComponent::reSortTable ( ) 
 

Triggers a resort of the table according to the current sortcolumn.If you modify the table's contents, you can call this to signal that the table needs to be resorted.(This doesn't do any sorting synchronously it just asynchronously sends a call to the tableSortOrderChanged() method of any listeners).