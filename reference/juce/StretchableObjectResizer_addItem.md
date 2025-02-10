#### addItem()


 void StretchableObjectResizer::addItem ( double currentSize, 
 
 double minSize, 
 double maxSize, 
 int order = 0 ) 

Adds an item to the list.The order parameter lets you specify groups of items that are resized first when some space needs to be found. Those items with an order of 0 will be the first ones to be resized, and if that doesn't provide enough space to meet the requirements, the algorithm will then try resizing the items with an order of 1, then 2, and so on.