#### getTopLevelTargetComponent()


 Component \* PopupMenu::Options::getTopLevelTargetComponent ( ) const noexcept 
 

Gets the target component that was set for the toplevel menu.When querying the options of a submenu, getTargetComponent() will always return nullptr, while getTopLevelTargetComponent() will return the target passed to withTargetComponent() when creating the toplevel menu.