#### addPopupMenuItems()


 virtual void CodeEditorComponent::addPopupMenuItems ( PopupMenu & menuToAddTo, const MouseEvent \* mouseClickEvent ) virtual 
 

This adds the items to the popup menu.By default it adds the cut/copy/paste items, but you can override this if you need to replace these with your own items.If you want to add your own items to the existing ones, you can override this, call the base class's addPopupMenuItems() method, then append your own items.When the menu has been shown, performPopupMenuAction() will be called to perform the item that the user has chosen.If this was triggered by a mouseclick, the mouseClickEvent parameter will be a pointer to the info about it, or may be null if the menu is being triggered by some other means.See alsoperformPopupMenuAction, setPopupMenuEnabled, isPopupMenuEnabled