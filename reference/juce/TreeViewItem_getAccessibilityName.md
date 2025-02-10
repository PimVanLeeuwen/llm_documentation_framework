#### getAccessibilityName()


 virtual String TreeViewItem::getAccessibilityName ( ) virtual 
 

Use this to set the name for this item that will be read out by accessibility clients.The default implementation will return the tooltip string from getTooltip() if it is not empty, otherwise it will return a description of the nested level and row number of the item.See alsoAccessibilityHandler