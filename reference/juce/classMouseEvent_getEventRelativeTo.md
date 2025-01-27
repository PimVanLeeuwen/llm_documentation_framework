#### getEventRelativeTo()


 MouseEvent MouseEvent::getEventRelativeTo ( Component \* newComponent ) const noexcept 
 

Creates a version of this event that is relative to a different component.The x and y positions of the event that is returned will have been adjusted to be relative to the new component. The component pointer that is passedin must not be null.