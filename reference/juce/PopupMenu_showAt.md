#### showAt() [2/2]


 int PopupMenu::showAt ( Component \* componentToAttachTo, 
 
 int itemIDThatMustBeVisible = 0, 
 int minimumWidth = 0, 
 int maximumNumColumns = 0, 
 int standardItemHeight = 0, 
 ModalComponentManager::Callback \* callback = nullptr ) 

Displays the menu as if it's attached to a component such as a button.This is similar to showAt(), but will position it next to the given component, e.g. so that the menu's edge is aligned with that of the component. This is intended for things like buttons that trigger a popup menu.