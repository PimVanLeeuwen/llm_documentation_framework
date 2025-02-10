#### withInitiallySelectedItem()


 Options PopupMenu::Options::withInitiallySelectedItem ( int idOfItemToBeSelected ) const nodiscard 
 

Sets an item to select in the menu.This is useful for controls such as combo boxes, where opening the combo box with the keyboard should ideally highlight the currentlyselected item, allowing the next/previous item to be selected by pressing up/down on the keyboard, rather than needing to move the highlighted row down from the top of the menu each time it is opened.