#### menuItemsChanged()


 void MenuBarModel::menuItemsChanged ( ) 
 

Call this when some of your menu items have changed.This method will cause a callback to any MenuBarListener objects that are registered with this model.If this model is displaying items from an ApplicationCommandManager, you can use the setApplicationCommandManagerToWatch() method to cause change messages to be sent automatically when the ApplicationCommandManager is changed.See alsoaddListener, removeListener, MenuBarListener