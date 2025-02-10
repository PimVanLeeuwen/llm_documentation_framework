#### setMultipleSelectionEnabled()


 void ListBox::setMultipleSelectionEnabled ( bool shouldBeEnabled ) noexcept 
 

Turns on multipleselection of rows.By default this is disabled.When your row component gets clicked you'll need to call the selectRowsBasedOnModifierKeys() method to tell the list that it's been clicked and to get it to do the appropriate selection based on whether the ctrl/shift keys are held down.