#### sortOrderChanged()


 virtual void TableListBoxModel::sortOrderChanged ( int newSortColumnId, bool isForwards ) virtual 
 

This callback is made when the table's sort order is changed.This could be because the user has clicked a column header, or because the TableHeaderComponent::setSortColumnId() method was called.If you implement this, your method should resort the table using the given column as the key.