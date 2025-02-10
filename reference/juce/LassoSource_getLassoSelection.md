#### getLassoSelection()


template<class SelectableItemType > 

 virtual SelectedItemSet< SelectableItemType > & LassoSource< SelectableItemType >::getLassoSelection ( ) pure virtual 
 

Returns the SelectedItemSet that the lasso should update.This set will be continuously updated by the LassoComponent as it gets dragged around, so make sure that you've got a ChangeListener attached to the set so that your UI objects will know when the selection changes and be able to update themselves appropriately.Referenced by LassoComponent< SelectableItemType >::beginLasso().