#### getDraggingMouseSource()


 MouseInputSource \* Desktop::getDraggingMouseSource ( int index ) const noexcept 
 

Returns one of the mouse sources that's currently being dragged.The index should be between 0 and getNumDraggingMouseSources() 1. If the index is out of range, or if no mice or fingers are down, this will return a null pointer.