#### selectOnly()


template<class SelectableItemType > 

 void SelectedItemSet< SelectableItemType >::selectOnly ( ParameterType item ) 
 

Clears any other currently selected items, and selects this item.If this item is already the only thing selected, no change notification will be sent out.See alsoaddToSelection, addToSelectionBasedOnModifiers References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::add(), SelectedItemSet< SelectableItemType >::changed(), SelectedItemSet< SelectableItemType >::deselect(), SelectedItemSet< SelectableItemType >::deselectAll(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getUnchecked(), SelectedItemSet< SelectableItemType >::isSelected(), SelectedItemSet< SelectableItemType >::itemSelected(), jmin(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::size().Referenced by SelectedItemSet< SelectableItemType >::addToSelectionBasedOnModifiers().