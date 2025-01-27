#### removeColumn()


 void TableHeaderComponent::removeColumn ( int columnIdToRemove ) 
 

Removes a column with the given ID.If there is such a column, this will asynchronously call the tableColumnsChanged() method of any registered listeners.