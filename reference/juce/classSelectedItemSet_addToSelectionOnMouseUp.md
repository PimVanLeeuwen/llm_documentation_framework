#### addToSelectionOnMouseUp()


template<class SelectableItemType > 

 void SelectedItemSet< SelectableItemType >::addToSelectionOnMouseUp ( ParameterType item, 
 
 ModifierKeys modifiers, 
 const bool wasItemDragged, 
 const bool resultOfMouseDownSelectMethod ) 

Selects or deselects items that can also be dragged, based on a mouseup event.Call this during a mouseUp callback, when you have previously called the addToSelectionOnMouseDown() method during your mouseDown event.See addToSelectionOnMouseDown() for more infoParameters

 item the item to select (or deselect) 
 
 modifiers the modifiers from the mouseup event 
 wasItemDragged true if your item was dragged during the mouse click 
 resultOfMouseDownSelectMethod this is the boolean return value that came back from the addToSelectionOnMouseDown() call that you should have made during the matching mouseDown event 


References SelectedItemSet< SelectableItemType >::addToSelectionBasedOnModifiers().