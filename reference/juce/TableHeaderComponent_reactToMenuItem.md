#### reactToMenuItem()


 virtual void TableHeaderComponent::reactToMenuItem ( int menuReturnId, int columnIdClicked ) virtual 
 

Override this to handle any custom items that you have added to the popup menu with an addMenuItems() override.If the menuReturnId isn't one of your own custom menu items, you'll need to call TableHeaderComponent::reactToMenuItem() to allow the base class to handle the items that it had added.See alsoaddMenuItems