#### setColumnVisible()


 void TableHeaderComponent::setColumnVisible ( int columnId, 
 
 bool shouldBeVisible ) 

Shows or hides a column.This can cause an asynchronous callback to the tableColumnsChanged() method of any registered listeners.See alsoisColumnVisible