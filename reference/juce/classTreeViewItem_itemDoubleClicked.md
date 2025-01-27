#### itemDoubleClicked()


 virtual void TreeViewItem::itemDoubleClicked ( const MouseEvent & ) virtual 
 

Called when the user doubleclicks on this item.If you're using createItemComponent() to create a custom component for the item, the mouseclicks might not make it through to the TreeView, but this is how you find out about clicks when just drawing each item individually.The associated mouseevent details are passed in, so you can find out about which button, where it was, etc.If not overridden, the base class method here will open or close the item as if the 'plus' button had been clicked.See alsoitemClicked