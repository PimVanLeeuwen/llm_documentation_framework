#### show()


 int PopupMenu::show ( int itemIDThatMustBeVisible = 0, 
 
 int minimumWidth = 0, 
 int maximumNumColumns = 0, 
 int standardItemHeight = 0, 
 ModalComponentManager::Callback \* callback = nullptr ) 

Displays the menu and waits for the user to pick something.This will display the menu modally, and return the ID of the item that the user picks. If they click somewhere off the menu to get rid of it without choosing anything, this will return 0.The current location of the mouse will be used as the position to show the menu to explicitly set the menu's position, use showAt() instead. Depending on where this point is on the screen, the menu will appear above, below or to the side of the point.Parameters

 itemIDThatMustBeVisible if you set this to the ID of one of the menu items, then when the menu first appears, it will make sure that this item is visible. So if the menu has too many items to fit on the screen, it will be scrolled to a position where this item is visible. 
 
 minimumWidth a minimum width for the menu, in pixels. It may be wider than this if some items are too long to fit. 
 maximumNumColumns if there are too many items to fit onscreen in a single vertical column, the menu may be laid out as a series of columns this is the maximum number allowed. To use the default value for this (probably about 7), you can pass in zero. 
 standardItemHeight if this is nonzero, it will be used as the standard height for menu items (apart from custom items) 
 callback if this is not a nullptr, the menu will be launched asynchronously, returning immediately, and the callback will receive a call when the menu is either dismissed or has an item selected. This object will be owned and deleted by the system, so make sure that it works safely and that any pointers that it uses are safely within scope. 



See alsoshowAt