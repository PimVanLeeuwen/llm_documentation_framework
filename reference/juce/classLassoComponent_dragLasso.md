#### dragLasso()


template<class SelectableItemType > 

 void LassoComponent< SelectableItemType >::dragLasso ( const MouseEvent & e ) 
 

Call this in your mouseDrag event, to update the lasso's position.This must be repeatedly calling when the mouse is dragged, after you've first initialised the lasso with beginLasso().This method takes into account the modifier keys that are being held down, so if shift is pressed, then the lassoed items will be added to any that were previously selected; if ctrl or command is pressed, then they will be xor'ed with previously selected items.See alsobeginLasso, endLasso References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::addArray(), Component::getBounds(), MouseEvent::getPosition(), ModifierKeys::isAltDown(), ModifierKeys::isCommandDown(), ModifierKeys::isShiftDown(), MouseEvent::mods, Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::removeValuesIn(), Component::setBounds(), and Component::setVisible().