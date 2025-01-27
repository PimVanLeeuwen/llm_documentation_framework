#### setModel()


 void BurgerMenuComponent::setModel ( MenuBarModel \* newModel ) 
 

Changes the model object to use to control the burger menu.This can be a nullptr, in which case the bar will be empty. This object will not be owned by the BurgerMenuComponent so it is up to you to manage its lifetime. Don't delete the object that is passedin while it's still being used by this MenuBar. Any submenus in your MenuBarModel will be recursively flattened and added to the toplevel burger menu section.