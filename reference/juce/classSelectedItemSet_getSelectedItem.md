#### getSelectedItem()


template<class SelectableItemType > 

 SelectableItemType SelectedItemSet< SelectableItemType >::getSelectedItem ( const int index ) const 
 

Returns one of the currently selected items.If the index is outofrange, this returns a defaultconstructed SelectableItemType.See alsogetNumSelected