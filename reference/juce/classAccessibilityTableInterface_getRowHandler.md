#### getRowHandler()


 virtual const AccessibilityHandler \* AccessibilityTableInterface::getRowHandler ( int row ) const pure virtual 
 

Returns the AccessibilityHandler for a row in the table, or nullptr if there is no row at this index.The row component should have a child component for each column in the table.