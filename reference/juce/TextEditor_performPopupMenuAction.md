#### performPopupMenuAction()


 virtual void TextEditor::performPopupMenuAction ( int menuItemID ) virtual 
 

This is called to perform one of the items that was shown on the popup menu.If you've overridden addPopupMenuItems(), you should also override this to perform the actions that you've added.If you've overridden addPopupMenuItems() but have still left the default items on the menu, remember to call the superclass's performPopupMenuAction() so that it can perform the default actions if that's what the user clicked on.See alsoaddPopupMenuItems, setPopupMenuEnabled, isPopupMenuEnabled