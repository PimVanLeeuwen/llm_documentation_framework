#### setMacMainMenu()


 static void MenuBarModel::setMacMainMenu ( MenuBarModel \* newMenuBarModel, const PopupMenu \* extraAppleMenuItems = nullptr, const String & recentItemsMenuName = String() ) static 
 

OSX ONLY Sets the model that is currently being shown as the main menu bar at the top of the screen on the Mac.You can pass nullptr to stop the current model being displayed. Be careful not to delete a model while it is being used.An optional extra menu can be specified, containing items to add to the top of the apple menu. (Confusingly, the 'apple' menu isn't the one with a picture of an apple, it's the one next to it, with your application's name at the top and the services menu etc on it). When one of these items is selected, the menu bar model will be used to invoke it, and in the menuItemSelected() callback the topLevelMenuIndex parameter will be 1. If you pass in an extraAppleMenuItems object then newMenuBarModel must be nonnull.If the recentItemsMenuName parameter is nonempty, then any submenus with this name will be replaced by OSX's special recentfiles menu.