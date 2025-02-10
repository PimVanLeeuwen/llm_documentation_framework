#### addCustomItem() [2/2]


 void PopupMenu::addCustomItem ( int itemResultID, 
 
 Component & customComponent, 
 int idealWidth, 
 int idealHeight, 
 bool triggerMenuItemAutomaticallyWhenClicked, 
 std::unique\_ptr< const PopupMenu > optionalSubMenu = nullptr, 
 const String & itemTitle = {} ) 

Appends a custom menu item that can't be used to trigger a result.This will add a userdefined component to use as a menu item. The caller must ensure that the passedin component stays alive until after the menu has been hidden.If triggerMenuItemAutomaticallyWhenClicked is true, the menu itself will handle detection of a mouseclick on your component, and use that to trigger the menu ID specified in itemResultID. If this is false, the menu item can't be triggered, so itemResultID is not used.itemTitle will be used as the fallback text for this item, and will be exposed to screen reader clients.Note that native macOS menus do not support custom components.