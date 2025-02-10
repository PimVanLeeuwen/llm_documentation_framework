#### addCommandItem()


 void PopupMenu::addCommandItem ( ApplicationCommandManager \* commandManager, 
 
 CommandID commandID, 
 String displayName = {}, 
 std::unique\_ptr< Drawable > iconToUse = {} ) 

Adds an item that represents one of the commands in a command manager object.Parameters

 commandManager the manager to use to trigger the command and get information about it 
 
 commandID the ID of the command 
 displayName if this is nonempty, then this string will be used instead of the command's registered name 
 iconToUse an optional Drawable object to use as the icon to the left of the item. The menu will take ownership of this drawable object and will delete it later when no longer needed