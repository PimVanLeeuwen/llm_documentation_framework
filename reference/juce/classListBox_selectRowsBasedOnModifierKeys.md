#### selectRowsBasedOnModifierKeys()


 void ListBox::selectRowsBasedOnModifierKeys ( int rowThatWasClickedOn, 
 
 ModifierKeys modifiers, 
 bool isMouseUpEvent ) 

Multiplyselects rows based on the modifier keys.If no modifier keys are down, this will select the given row and deselect any others.If the ctrl (or command on the Mac) key is down, it'll flip the state of the selected row.If the shift key is down, it'll select up to the given row from the last row selected.See alsoselectRow