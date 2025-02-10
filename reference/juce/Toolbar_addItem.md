#### addItem()


 void Toolbar::addItem ( ToolbarItemFactory & factory, 
 
 int itemId, 
 int insertIndex = 1 ) 

Adds an item to the toolbar.The factory's ToolbarItemFactory::createItem() will be called by this method to create the component that will actually be added to the bar.The new item will be inserted at the specified index (if the index is 1, it will be added to the righthand or bottom end of the bar).Once added, the component will be automatically deleted by this object when it is no longer needed.See alsoToolbarItemFactory