#### addItem() [6/6]


 void PopupMenu::addItem ( int itemResultID, 
 
 String itemText, 
 bool isEnabled, 
 bool isTicked, 
 std::unique\_ptr< Drawable > iconToUse ) 

Appends a new item with an icon.Parameters

 itemResultID the number that will be returned from the show() method if the user picks this item. The value should never be zero, because that's used to indicate that the user didn't select anything. 
 
 itemText the text to show. 
 isEnabled if false, the item will be shown 'greyedout' and can't be picked 
 isTicked if true, the item will be shown with a tick next to it 
 iconToUse a Drawable object to use as the icon to the left of the item. The menu will take ownership of this drawable object and will delete it later when no longer needed 



See alsoaddSeparator, addColouredItem, addCustomItem, addSubMenu