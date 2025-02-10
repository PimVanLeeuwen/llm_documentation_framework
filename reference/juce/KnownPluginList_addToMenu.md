#### addToMenu()


 static void KnownPluginList::addToMenu ( PopupMenu & menu, const Array< PluginDescription > & types, SortMethod sortMethod, const String & currentlyTickedPluginID = {} ) static 
 

Adds the plugin types to a popup menu so that the user can select one.Depending on the sort method, it may add submenus for categories, manufacturers, etc.Use getIndexChosenByMenu() to find out the type that was chosen.