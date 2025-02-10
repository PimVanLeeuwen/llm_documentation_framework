#### setLookAndFeel()


 void PopupMenu::setLookAndFeel ( LookAndFeel \* newLookAndFeel ) 
 

Specifies a lookandfeel for the menu and any submenus that it has.This can be called before show() if you need a customised menu. Be careful not to delete the LookAndFeel object before the menu has been deleted.