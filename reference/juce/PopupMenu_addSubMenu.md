#### addSubMenu() [3/3]


 void PopupMenu::addSubMenu ( String subMenuName, 
 
 PopupMenu subMenu, 
 bool isEnabled, 
 std::unique\_ptr< Drawable > iconToUse, 
 bool isTicked = false, 
 int itemResultID = 0 ) 

Appends a submenu with an icon.If the menu that's passed in is empty, it will appear as an inactive item. If the itemResultID argument is nonzero, then the submenu item itself can be clicked to trigger it as a command.The iconToUse parameter is a Drawable object to use as the icon to the left of the item. The menu will take ownership of this drawable object and will delete it later when no longer needed