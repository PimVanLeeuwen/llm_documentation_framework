#### itemSelected()


template<class SelectableItemType > 

 virtual void SelectedItemSet< SelectableItemType >::itemSelected ( SelectableItemType ) virtual 
 

Can be overridden to do special handling when an item is selected.For example, if the item is an object, you might want to call it and tell it that it's being selected.Referenced by SelectedItemSet< SelectableItemType >::addToSelection(), SelectedItemSet< SelectableItemType >::operator=(), and SelectedItemSet< SelectableItemType >::selectOnly().