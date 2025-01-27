#### addColumn()


 void TableHeaderComponent::addColumn ( const String & columnName, 
 
 int columnId, 
 int width, 
 int minimumWidth = 30, 
 int maximumWidth = 1, 
 int propertyFlags = defaultFlags, 
 int insertIndex = 1 ) 

Adds a column to the table.This will add a column, and asynchronously call the tableColumnsChanged() method of any registered listeners.Parameters

 columnName the name of the new column. It's ok to have two or more columns with the same name 
 
 columnId an ID for this column. The ID can be any number apart from 0, but every column must have a unique ID. This is used to identify the column later on, after the user may have changed the order that they appear in 
 width the initial width of the column, in pixels 
 maximumWidth a maximum width that the column can take when the user is resizing it. This only applies if the 'resizable' flag is specified for this column 
 minimumWidth a minimum width that the column can take when the user is resizing it. This only applies if the 'resizable' flag is specified for this column 
 propertyFlags a combination of some of the values from the ColumnPropertyFlags enum, to define the properties of this column 
 insertIndex the index at which the column should be added. A value of 0 puts it at the start (lefthand side) and 1 puts it at the end (righthand size) of the table. Note that the index the index within all columns, not just the index amongst those that are currently visible