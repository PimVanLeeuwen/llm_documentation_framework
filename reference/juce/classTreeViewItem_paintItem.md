#### paintItem()


 virtual void TreeViewItem::paintItem ( Graphics & g, int width, int height ) virtual 
 

Draws the item's contents.You can choose to either implement this method and draw each item, or you can use createItemComponent() to create a component that will represent the item.If all you need in your tree is to be able to draw the items and detect when the user selects or doubleclicks one of them, it's probably enough to use paintItem(), itemClicked() and itemDoubleClicked(). If you need more complicated interactions, you may need to use createItemComponent() instead.Parameters

 g the graphics context to draw into 
 
 width the width of the area available for drawing 
 height the height of the area available for drawing