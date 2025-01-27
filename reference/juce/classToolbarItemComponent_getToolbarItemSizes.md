#### getToolbarItemSizes()


 virtual bool ToolbarItemComponent::getToolbarItemSizes ( int toolbarThickness, bool isToolbarVertical, int & preferredSize, int & minSize, int & maxSize ) pure virtual 
 

This method must return the size criteria for this item, based on a given toolbar size and orientation.The preferredSize, minSize and maxSize values must all be set by your implementation method. If the toolbar is horizontal, these will be the width of the item; for a vertical toolbar, they refer to the item's height.The preferredSize is the size that the component would like to be, and this must be between the min and max sizes. For a fixedsize item, simply set all three variables to the same value.The toolbarThickness parameter tells you the depth of the toolbar the same as calling Toolbar::getThickness().The isToolbarVertical parameter tells you whether the bar is oriented horizontally or vertically.Implemented in ToolbarButton.