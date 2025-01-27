#### isPopupMenu()


 bool ModifierKeys::isPopupMenu ( ) const noexcept 
 

Checks whether the user is trying to launch a popup menu.This checks for platformspecific modifiers that might indicate that the user is following the operating system's normal method of showing a popup menu.So on Windows/Linux, this method is really testing for a rightclick. On the Mac, it tests for either the CTRL key being down, or a rightclick.Referenced by SelectedItemSet< SelectableItemType >::addToSelectionOnMouseDown().