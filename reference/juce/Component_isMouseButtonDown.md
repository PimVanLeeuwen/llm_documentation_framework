#### isMouseButtonDown()


 bool Component::isMouseButtonDown ( bool includeChildren = false ) const 
 

Returns true if the mouse button is currently held down in this component.Note that this is a test to see whether the mouse is being pressed in this component, so it'll return false if called on component A when the mouse is actually being dragged in component B.See alsoisMouseButtonDownAnywhere, isMouseOver, isMouseOverOrDragging