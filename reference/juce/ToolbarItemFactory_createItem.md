#### createItem()


 virtual ToolbarItemComponent \* ToolbarItemFactory::createItem ( int itemId ) pure virtual 
 

Must create an instance of one of the items that the factory lists in its getAllToolbarItemIds() method.The itemId parameter can be any of the values listed by your getAllToolbarItemIds() method, except for the builtin item types from the SpecialItemIds enum, which are created internally by the toolbar code.Try not to keep a pointer to the object that is returned, as it will be deleted automatically by the toolbar, and remember that multiple instances of the same item type are likely to exist at the same time.