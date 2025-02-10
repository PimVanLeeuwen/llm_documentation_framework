#### getPosition()


 Point< int > MouseEvent::getPosition ( ) const noexcept 
 

The position of the mouse when the event occurred.This position is relative to the topleft of the component to which the event applies (as indicated by the MouseEvent::eventComponent field).For a floatingpoint position, see MouseEvent::positionReferenced by LassoComponent< SelectableItemType >::dragLasso().