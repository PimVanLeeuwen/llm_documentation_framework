#### getMouseDownPosition()


 Point< int > MouseEvent::getMouseDownPosition ( ) const noexcept 
 

Returns the coordinates of the last place that a mouse was pressed.The coordinates are relative to the component specified in MouseEvent::component. For a floating point version of this value, see mouseDownPosition.See alsomouseDownPosition, getDistanceFromDragStart, getDistanceFromDragStartX, mouseWasDraggedSinceMouseDown Referenced by LassoComponent< SelectableItemType >::beginLasso().