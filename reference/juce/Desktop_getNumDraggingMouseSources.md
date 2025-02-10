#### getNumDraggingMouseSources()


 int Desktop::getNumDraggingMouseSources ( ) const noexcept 
 

Returns the number of mousesources that are currently being dragged.In a traditional singlemouse system, this will be 0 or 1, depending on whether a JUCE component has the button down on it. In a multitouch system, this could be any number from 0 to the number of simultaneous touches that can be detected.