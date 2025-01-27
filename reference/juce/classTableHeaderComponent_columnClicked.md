#### columnClicked()


 virtual void TableHeaderComponent::columnClicked ( int columnId, const ModifierKeys & mods ) virtual 
 

This can be overridden to handle a mouseclick on one of the column headers.The default implementation will use this click to call getSortColumnId() and change the sort order.