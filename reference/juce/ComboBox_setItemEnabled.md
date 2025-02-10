#### setItemEnabled()


 void ComboBox::setItemEnabled ( int itemId, 
 
 bool shouldBeEnabled ) 

This allows items in the dropdown list to be selectively disabled.When you add an item, it's enabled by default, but you can call this method to change its status.If you disable an item which is already selected, this won't change the current selection it just stops the user choosing that item from the list.