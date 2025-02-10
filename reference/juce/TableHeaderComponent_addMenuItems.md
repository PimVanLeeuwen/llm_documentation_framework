#### addMenuItems()


 virtual void TableHeaderComponent::addMenuItems ( PopupMenu & menu, int columnIdClicked ) virtual 
 

This can be overridden to add custom items to the popup menu.If you override this, you should call the superclass's method to add its column show/hide items, if you want them on the menu as well.Then to handle the result, override reactToMenuItem().See alsoreactToMenuItem