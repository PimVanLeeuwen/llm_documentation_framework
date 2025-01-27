#### itemDeselected()


template<class SelectableItemType > 

 virtual void SelectedItemSet< SelectableItemType >::itemDeselected ( SelectableItemType ) virtual 
 

Can be overridden to do special handling when an item is deselected.For example, if the item is an object, you might want to call it and tell it that it's being deselected.Referenced by SelectedItemSet< SelectableItemType >::deselect(), SelectedItemSet< SelectableItemType >::deselectAll(), and SelectedItemSet< SelectableItemType >::operator=().