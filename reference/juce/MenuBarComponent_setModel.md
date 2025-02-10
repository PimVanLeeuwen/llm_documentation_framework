#### setModel()


 void MenuBarComponent::setModel ( MenuBarModel \* newModel ) 
 

Changes the model object to use to control the bar.This can be a null pointer, in which case the bar will be empty. Don't delete the object that is passedin while it's still being used by this MenuBar.