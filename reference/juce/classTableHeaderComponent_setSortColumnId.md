#### setSortColumnId()


 void TableHeaderComponent::setSortColumnId ( int columnId, 
 
 bool sortForwards ) 

Changes the column which is the sort column.This can cause an asynchronous callback to the tableSortOrderChanged() method of any registered listeners.If this method doesn't actually change the column ID, then no resort will take place (you can call reSortTable() to force a resort to happen if you've modified the table's contents).See alsogetSortColumnId, isSortedForwards, reSortTable