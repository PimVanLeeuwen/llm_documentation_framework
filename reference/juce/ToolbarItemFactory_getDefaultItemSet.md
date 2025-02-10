#### getDefaultItemSet()


 virtual void ToolbarItemFactory::getDefaultItemSet ( Array< int > & ids ) pure virtual 
 

Must return the set of items that should be added to a toolbar as its default set.This method is used by Toolbar::addDefaultItems() to determine which items to create.The items that your method adds to the array that is passedin will be added to the toolbar in the same order. Items can appear in the list more than once.