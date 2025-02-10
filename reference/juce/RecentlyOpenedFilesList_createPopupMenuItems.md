#### createPopupMenuItems()


 int RecentlyOpenedFilesList::createPopupMenuItems ( PopupMenu & menuToAddItemsTo, 
 
 int baseItemId, 
 bool showFullPaths, 
 bool dontAddNonExistentFiles, 
 const File \*\* filesToAvoid = nullptr ) 

Adds entries to a menu, representing each of the files in the list.This is handy for creating an "open recent file..." menu in your app. The menu items are numbered consecutively starting with the baseItemId value, and can either be added as complete pathnames, or just the last part of the filename.If dontAddNonExistentFiles is true, then each file will be checked and only those that exist will be added.If filesToAvoid is not a nullptr, then it is considered to be a zeroterminated array of pointers to file objects. Any files that appear in this list will not be added to the menu the reason for this is that you might have a number of files already open, so might not want these to be shown in the menu.It returns the number of items that were added.