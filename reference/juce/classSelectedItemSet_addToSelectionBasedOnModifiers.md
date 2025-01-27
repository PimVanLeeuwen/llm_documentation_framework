#### addToSelectionBasedOnModifiers()


template<class SelectableItemType > 

 void SelectedItemSet< SelectableItemType >::addToSelectionBasedOnModifiers ( ParameterType item, 
 
 ModifierKeys modifiers ) 

Selects or deselects an item.This will use the modifier keys to decide whether to deselect other items first.So if the shift key is held down, the item will be added without deselecting anything (same as calling addToSelection() )If no modifiers are down, the current selection will be cleared first (same as calling selectOnly() )If the ctrl (or command on the Mac) key is held down, the item will be toggled so it'll be added to the set unless it's already there, in which case it'll be deselected.If the items that you're selecting can also be dragged, you may need to use the addToSelectionOnMouseDown() and addToSelectionOnMouseUp() calls to handle the subtleties of this kind of usage.See alsoselectOnly, addToSelection, addToSelectionOnMouseDown, addToSelectionOnMouseUp References SelectedItemSet< SelectableItemType >::addToSelection(), SelectedItemSet< SelectableItemType >::deselect(), ModifierKeys::isCommandDown(), SelectedItemSet< SelectableItemType >::isSelected(), ModifierKeys::isShiftDown(), and SelectedItemSet< SelectableItemType >::selectOnly().Referenced by SelectedItemSet< SelectableItemType >::addToSelectionOnMouseDown(), and SelectedItemSet< SelectableItemType >::addToSelectionOnMouseUp().