#### addToSelectionOnMouseDown()


template<class SelectableItemType > 

 bool SelectedItemSet< SelectableItemType >::addToSelectionOnMouseDown ( ParameterType item, 
 
 ModifierKeys modifiers ) 

Selects or deselects items that can also be dragged, based on a mousedown event.If you call addToSelectionOnMouseDown() at the start of your mouseDown event, and then call addToSelectionOnMouseUp() at the end of your mouseUp event, this makes it easy to handle multipleselection of sets of objects that can also be dragged.For example, if you have several items already selected, and you click on one of them (without dragging), then you'd expect this to deselect the other, and just select the item you clicked on. But if you had clicked on this item and dragged it, you'd have expected them all to stay selected.When you call this method, you'll need to store the boolean result, because the addToSelectionOnMouseUp() method will need to be know this value.See alsoaddToSelectionOnMouseUp, addToSelectionBasedOnModifiers References SelectedItemSet< SelectableItemType >::addToSelectionBasedOnModifiers(), ModifierKeys::isPopupMenu(), and SelectedItemSet< SelectableItemType >::isSelected().