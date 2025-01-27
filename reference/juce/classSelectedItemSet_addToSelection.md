#### addToSelection()


template<class SelectableItemType > 

 void SelectedItemSet< SelectableItemType >::addToSelection ( ParameterType item ) 
 

Selects an item.If the item is already selected, no change notification will be sent out.See alsoselectOnly, addToSelectionBasedOnModifiers References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::add(), SelectedItemSet< SelectableItemType >::changed(), SelectedItemSet< SelectableItemType >::isSelected(), and SelectedItemSet< SelectableItemType >::itemSelected().Referenced by SelectedItemSet< SelectableItemType >::addToSelectionBasedOnModifiers().