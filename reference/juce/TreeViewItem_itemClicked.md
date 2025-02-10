#### itemClicked()


 virtual void TreeViewItem::itemClicked ( const MouseEvent & ) virtual 
 

Called when the user clicks on this item.If you're using createItemComponent() to create a custom component for the item, the mouseclicks might not make it through to the TreeView, but this is how you find out about clicks when just drawing each item individually.The associated mouseevent details are passed in, so you can find out about which button, where it was, etc.See alsoitemDoubleClicked