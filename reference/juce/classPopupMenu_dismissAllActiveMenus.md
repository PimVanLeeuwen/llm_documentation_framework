#### dismissAllActiveMenus()


 static bool JUCE\_CALLTYPE PopupMenu::dismissAllActiveMenus ( ) static 
 

Closes any menus that are currently open.This might be useful if you have a situation where your window is being closed by some means other than a user action, and you'd like to make sure that menus aren't left hanging around.